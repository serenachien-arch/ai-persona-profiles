#!/usr/bin/env python3
"""題庫機器檢查：抓出題目裡不該出現的東西。

用法：python3 tools/check_question_bank.py
沒有問題時結束碼為 0，有問題時列出每一題並以結束碼 1 結束。
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent / "question-bank"

# 題目只給方向，不給事實：不能有數字、真實工具或公司名稱、時事字眼。
RULES = [
    (re.compile(r"[0-9０-９%％$]"), "有數字或百分比（數字只能由人設寫自己經驗裡的）"),
    (re.compile(
        r"ChatGPT|GPT|OpenAI|Claude|Anthropic|Gemini|Google|Copilot|Microsoft|"
        r"Meta|Threads|Instagram|Facebook|AWS|Azure|GCP|Notion|Slack|Figma|"
        r"React|Vue|Angular|Kubernetes|Docker|GitHub|GitLab|Midjourney|"
        r"Apple|iPhone|Android|Shopee|Grab|Tokopedia|Gojek|LINE",
        re.I), "有真實工具、平台或公司名稱"),
    (re.compile(r"最近|今天|昨天|今年|上個月|新聞|剛推出|最新版|新功能上線"),
     "有時效字眼（會過期，或引人寫時事）"),
    (re.compile(r"價格|方案|訂閱費|費用|多少錢|金額(?!）)"), "有價格相關字眼"),
]
MAX_LEN = 60  # 題目方向超過這個長度，通常是塞了太多細節

ROW = re.compile(r"^\| (Q\d{2}-\d{3}) \| (.+?) \| (.+?) \| (.+?) \|$")


def main() -> int:
    problems, seen, total = [], {}, 0
    for path in sorted(ROOT.glob("[0-9][0-9]-*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if not m:
                continue
            total += 1
            qid, question = m.group(1), m.group(2)
            # 括號裡的備註（例如「不點名」「不講金額」）是給人設的提醒，不算題目內容
            body = re.sub(r"（[^）]*）", "", question)
            for pattern, reason in RULES:
                if pattern.search(body):
                    problems.append(f"{path.name} {qid}：{reason}｜{question}")
            if len(body) > MAX_LEN:
                problems.append(f"{path.name} {qid}：超過 {MAX_LEN} 字｜{question}")
            if qid in seen:
                problems.append(f"{path.name} {qid}：編號重複（另見 {seen[qid]}）")
            seen[qid] = path.name
    for p in problems:
        print(p)
    print(f"檢查 {total} 題，問題 {len(problems)} 個")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
