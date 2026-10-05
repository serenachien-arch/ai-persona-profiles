# 自動發文

[← 回總覽](../README.md)

每天晚上 **20:47（台北時間）** 由排程任務「Threads 人設每日自動發文」（Routine）叫醒 Claude 的工作階段，照下面的步驟產生隔天的貼文並排進 Metricool。

- **早上備援**：每天早上 **08:47（台北時間）** 還有一個排程任務「Threads 人設發文備援（早上）」，補排**當天**還沒排到的時段（例如晚上那次中途卡住）。它會先查重複，晚上已經排好的話什麼都不做；發文時間已經過了或不到 15 分鐘的時段會跳過。
- **改每天發文的時間**：改下面「已啟用的人設」表裡的「每日發文時間」，下一次執行就會照新時間排。
- **暫停或停止**：在 claude.ai 的 Routines 頁面關掉這個排程任務，或直接跟 Claude 說。**這份文件就是排程任務的工作指示**，要改發文規則，改這裡就好。

## 已啟用的人設

| 人設 | Metricool 品牌 | blogId | Threads | 時區 | 每日發文時間 |
|---|---|---|---|---|---|
| [Jasmine Lin](../personas/01-jasmine-lin.md) | Jasmine Lin林禹茉 | 7182856 | jasmine.lin0222 | Asia/Taipei | 11:00、17:00 |

新增人設時，在這張表加一列，並建立 `posting-log/<編號>-<名字>.md`。

## 每次執行的步驟

每次執行（晚上 20:47、早上 08:47）都**檢查從今天起 3 天內的所有時段**，把還沒排的補上。Metricool 裡隨時會有約 3 天份的貼文，某一次執行中斷，後面兩天還是會照常發。

- 發文時間已經過了，或離現在不到 15 分鐘的時段：跳過，不補發（除非使用者要求）。
- 自動執行時不要停下來問使用者，也不要做到一半就結束，一定要把該排的排完。

對上表每一個人設、每一個時段，依序做：

1. **先查重複**：用 `getScheduledPosts` 查這個品牌今天起 3 天內的排程，並看 `posting-log` 有沒有這個日期、這個時段的紀錄。任一邊已經有 → 跳過，不要重複排。
2. **挑題目**：讀 `question-bank/<人設>.md` 和 `posting-log/<人設>.md`。
   - 從還沒用過的題目裡，挑編號最小、而且「建議反應」跟上一則**不一樣**的那題。
   - 全部用完 → 這個人設不要發文，在執行結果寫明「題庫用完」。
3. **寫貼文**：讀 `prompts/<人設>.txt`，把它當成 system prompt，用挑到的題目寫一則貼文。同一天的兩則不要寫成同一種開頭或結構。
4. **檢查**，全部通過才能排程，沒過就重寫：
   - 字數：先把貼文存成 `posting-log/drafts/<日期>-<時段>.txt`（這個資料夾不進 git），再跑 `python3 tools/count_post.py <檔案>`。中文人設 150〜200 字（不含空白和換行）；英文人設 450 字元以內；西班牙文／越南文／印尼文 400 字元以內（外語都含空格與標點）
   - 沒有違反 prompt 的【你絕對不講】
   - 沒有真實的工具名稱、公司名稱、價格、沒出處的數字
   - 沒有 hashtag，沒有「留言告訴我」這類呼籲
   - emoji 數量符合人設設定
   - 結構照該人設 prompt 的【怎麼寫】（Jasmine：讓人停下來的第一句 → 自己的小故事 → 「我後來才發現」的一個小發現，不用老師口吻）
5. **排程**：用 `createScheduledPost` 排進 Metricool（排在該時段的日期與時間）。
   - `providers`: `[{"network":"threads"}]`
   - `draft`: false，`autoPublish`: true
   - `publicationDate`: 該時段的發文時間，時區用上表
   - `threadsData`: `{"replyControl":"EVERYONE","type":"POST","shareAsInstagramStory":false}`
6. **記錄**：在 `posting-log/<人設>.md` 加一列（發佈時間、題號、建議反應、uuid、第一句）。

全部做完後：

> 自動執行時不需要人按同意：Metricool 查詢與排程、上面這些 git 指令、`tools/` 裡的兩個檢查腳本、編輯 `posting-log/`，都已在 `.claude/settings.json` 預先允許。修改或刪除 Metricool 裡已存在的貼文**沒有**預先允許，一定會先問。

7. 跑 `python3 tools/check_question_bank.py`，確認題庫檢查通過。
8. 照這三個指令 commit 並 push（這些指令已在 `.claude/settings.json` 預先允許，不會跳出確認）：
   - `git add posting-log/*`
   - `git commit -m "<訊息>"`
   - `git push -q origin claude/cool-curie-3tbq0c`
9. 回報：每則排了什麼時間、用哪一題、第一句是什麼；每個人設還剩幾題沒用。剩不到 6 題（約 3 天份）時，提醒要補題庫。

## 出錯時

- Metricool 排程失敗 → 不要重試超過一次，不要寫進發文紀錄，在回報裡寫明錯誤。
- 不確定一則貼文有沒有違規 → 不要排，換一題重寫。
