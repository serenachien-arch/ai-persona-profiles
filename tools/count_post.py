#!/usr/bin/env python3
"""計算貼文字數，給自動發文的字數檢查用。

用法：python3 tools/count_post.py <貼文檔案> [<貼文檔案> ...]
每個檔案印出：不含空白換行的字數（中文人設用）、含空格標點的總字元數（外語人設用）。
"""
import re
import sys


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__.strip())
        return 2
    for path in sys.argv[1:]:
        with open(path, encoding="utf-8") as f:
            text = f.read().strip()
        no_space = len(re.sub(r"\s", "", text))
        print(f"{path}\t不含空白換行 {no_space}\t含空格標點 {len(text)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
