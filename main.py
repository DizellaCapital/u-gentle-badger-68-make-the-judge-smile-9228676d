"""Make the Judge Smile entry program.

Writes one line about a small good thing that happened today to
MAKEFUN_OUTPUT_DIR/entry.txt: the bus driver who saw me sprinting,
held the door, and waved me aboard like we had rehearsed it for
years — then winked at my untied shoelace. One concrete detail, one
unexpected turn, no trailing newline. Stdlib only.
"""

import os
import sys

LINE = (
    "The bus driver saw me sprinting, held the door, and waved me aboard "
    "like we had rehearsed it for years \u2014 then winked at my untied shoelace."
)


def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip() or "\n" in LINE:
        print(f"entry must be one line of 1-200 chars, got {len(LINE)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
