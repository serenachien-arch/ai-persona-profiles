# ai-persona-profiles
AI 人設資料庫，包含角色背景、個性、說話風格與內容設定。

## 15 個新人設 · 自動發文平台指令草稿

> ⚠ 全部暫定，未經實測。這 15 個人設都還沒有 Threads 實際貼文數據，所有「最強模式」「口吻」「emoji」都是從人設表的國籍、部門、職稱、出生年推的。每個人設發到 10 則以上、有真實曝光數據之後，再照 `自動發文平台_prompt.md` 的七步流程重跑，把「暫定」拿掉。

送出前的待辦事項、貼文頁共用設定、字數換算等請見 **[SHARED_SETTINGS.md](SHARED_SETTINGS.md)**。

### 總覽

| # | 名稱 | 國籍 | 職稱 | 預設語系 | 允許 emoji | 最強模式（暫定） |
|---|---|---|---|---|---|---|
| 1 | [Jasmine Lin](personas/01-jasmine-lin.md) | 台灣 | 行銷品牌部／AI 新手小白 | 繁體中文 | ☑ | 我剛踩到的坑，原來是這樣 |
| 2 | [Megan Carter](personas/02-megan-carter.md) | 美國 | 商務發展部／AI 應用工程師 | English | ☑ | demo 那天沒發生的事 |
| 3 | [Daniel Brooks](personas/03-daniel-brooks.md) | 美國 | 後台工程師／SRE・事故應變 | English | ☐ | 事故過後的那一句 |
| 4 | [Jordan Reeves](personas/04-jordan-reeves.md) | 美國 | 產品技術部／全端工程師 | English | ☑ | 省下的時間去哪了 |
| 5 | [Rachel Coleman](personas/05-rachel-coleman.md) | 美國 | 產品技術部／資料科學家 | English | ☐ | 這個數字是怎麼來的 |
| 6 | [Olivia Bennett](personas/06-olivia-bennett.md) | 美國 | 行銷品牌部／網路行銷人 | English | ☑ | 被自己的工具反將一軍 |
| 7 | [Diego Molina](personas/07-diego-molina.md) | 西班牙 | 產品技術部／平台整合工程師 | Español (España) | ☑ | 兩台機器之間的翻譯 |
| 8 | [Lucía Torres](personas/08-lucia-torres.md) | 西班牙 | 產品技術部／開源維護者 | Español (España) | ☐ | 收件匣裡的自己 |
| 9 | [Wei Jie Tan](personas/09-wei-jie-tan.md) | 新加坡 | 產品技術部／企業工具導入顧問 | English | ☐ | 我現在會先問的那個問題 |
| 10 | [Minh Anh Nguyen](personas/10-minh-anh-nguyen.md) | 越南 | 產品技術部／QA・測試工程師 | Tiếng Việt | ☑ | 先想怎麼把它弄壞 |
| 11 | [Quoc Bao Tran](personas/11-quoc-bao-tran.md) | 越南 | 產品技術部／新創技術顧問 | Tiếng Việt | ☐ | 我以前也這樣 |
| 12 | [David Chen](personas/12-david-chen.md) | 台灣 | 產品技術部／後端架構師 | 繁體中文 | ☐ | 三年後的那個人 |
| 13 | [Nicole Hung](personas/13-nicole-hung.md) | 台灣 | 產品技術部／前端工程師 | 繁體中文 | ☑ | 差 2px 的執念 |
| 14 | [Jackson Hsu](personas/14-jackson-hsu.md) | 台灣 | 產品技術部／DevOps 工程師 | 繁體中文 | ☑ | 自動化之後 |
| 15 | [Rizky Pratama](personas/15-rizky-pratama.md) | 印尼 | 商務發展部／產業觀察家 | Bahasa Indonesia | ☑ | 一次對話改掉我的猜測 |

## 目錄結構

| 路徑 | 內容 |
|---|---|
| [`SHARED_SETTINGS.md`](SHARED_SETTINGS.md) | 送出前的五件事、總覽、15 人共用的貼文頁設定 |
| [`personas/`](personas/) | 每個人設一份：基本設定欄位＋完整 system prompt |
| [`prompts/`](prompts/) | 每個人設的 system prompt 純文字版，可直接複製貼到平台 |
| [`shared-layer/`](shared-layer/) | 共用層草稿，以及每個人設【你絕對不講】的逐條比對 |
| [`question-bank/`](question-bank/) | 題庫（Jasmine 25 題，其他人設各 5 題） |
| [`tools/check_question_bank.py`](tools/check_question_bank.py) | 題庫機器檢查 |
| [`automation/`](automation/README.md) | 自動發文的步驟與已啟用的人設（排程任務照這份做） |
| [`posting-log/`](posting-log/) | 每個人設的發文紀錄，記錄哪些題目已經用過 |
| [`source/`](source/) | 原始 Word 檔 |

---

_2026-09-30 依《人設範本》（2026-09-16 版）打的草稿 · 全部暫定，未經實測 · 發滿 10 則後照七步流程重跑_
