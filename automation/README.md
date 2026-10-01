# 自動發文

[← 回總覽](../README.md)

每天由排程任務（Routine）開一個新的工作階段，照下面的步驟產生貼文並排進 Metricool。**這份文件就是排程任務的工作指示**，要改發文規則，改這裡就好。

## 已啟用的人設

| 人設 | Metricool 品牌 | blogId | Threads | 時區 | 每日發文時間 |
|---|---|---|---|---|---|
| [Jasmine Lin](../personas/01-jasmine-lin.md) | Jasmine Lin林禹茉 | 7182856 | jasmine.lin0222 | Asia/Taipei | 11:00、17:00 |

新增人設時，在這張表加一列，並建立 `posting-log/<編號>-<名字>.md`。

## 每次執行的步驟

排程任務每天晚上執行一次，替**隔天**排好所有時段的貼文。晚上先排好，萬一出錯，發佈前還有時間處理；也可以在 Metricool 行事曆先看到隔天的內容。

對上表每一個人設、每一個時段，依序做：

1. **先查重複**：用 `getScheduledPosts` 查這個品牌隔天的排程。這個時段已經有貼文 → 跳過，不要重複排。
2. **挑題目**：讀 `question-bank/<人設>.md` 和 `posting-log/<人設>.md`。
   - 從還沒用過的題目裡，挑編號最小、而且「建議反應」跟上一則**不一樣**的那題。
   - 全部用完 → 這個人設不要發文，在執行結果寫明「題庫用完」。
3. **寫貼文**：讀 `prompts/<人設>.txt`，把它當成 system prompt，用挑到的題目寫一則貼文。同一天的兩則不要寫成同一種開頭或結構。
4. **檢查**，全部通過才能排程，沒過就重寫：
   - 字數：中文人設 150〜200 字（不含空白和換行）；英文人設 450 字元以內；西班牙文／越南文／印尼文 400 字元以內（外語都含空格與標點）
   - 沒有違反 prompt 的【你絕對不講】
   - 沒有真實的工具名稱、公司名稱、價格、沒出處的數字
   - 沒有 hashtag，沒有「留言告訴我」這類呼籲
   - emoji 數量符合人設設定
   - 第一句就是具體的瞬間，結尾沒有外掛教學結論
5. **排程**：用 `createScheduledPost` 排進 Metricool。
   - `providers`: `[{"network":"threads"}]`
   - `draft`: false，`autoPublish`: true
   - `publicationDate`: 隔天的發文時間，時區用上表
   - `threadsData`: `{"replyControl":"EVERYONE","type":"POST","shareAsInstagramStory":false}`
6. **記錄**：在 `posting-log/<人設>.md` 加一列（發佈時間、題號、建議反應、uuid、第一句）。

全部做完後：

7. 跑 `python3 tools/check_question_bank.py`，確認題庫檢查通過。
8. commit 並 push 到 `claude/cool-curie-3tbq0c` 分支。
9. 回報：每則排了什麼時間、用哪一題、第一句是什麼；每個人設還剩幾題沒用。剩不到 6 題（約 3 天份）時，提醒要補題庫。

## 出錯時

- Metricool 排程失敗 → 不要重試超過一次，不要寫進發文紀錄，在回報裡寫明錯誤。
- 不確定一則貼文有沒有違規 → 不要排，換一題重寫。
