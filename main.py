#!/usr/bin/env python3
"""One Line, Big Laugh entry (v2).

Writes a single hilarious line (<= 200 chars) to /output/entry.txt.
The line must land entirely on its own: no title, setup or explanation.
"""
import os

LINE = "I asked my AI to act more human, so it ghosted me for a week and texted 'u up?' at 3 a.m."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {len(LINE)} characters to /output/entry.txt")

if __name__ == "__main__":
    main()
