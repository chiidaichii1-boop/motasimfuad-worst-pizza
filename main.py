"""Write one funny line pitching the worst pizza topping to entry.txt.

The line is a single sentence, well under the 200-character gate.
"""

import os

LINE = (
    "New: the Regret Special \u2014 a pizza topped with cold baked beans "
    "and a single anchovy that stares at you like it knows what you did."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
