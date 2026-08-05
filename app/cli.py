"""Tiny command-line interface, so there is something to actually run.

Examples:
    python -m app.cli greet Ada
    python -m app.cli add 2 3
    python -m app.cli multiply 6 7
"""

import sys

from app import calculator, greetings

OPERATIONS = {
    "add": calculator.add,
    "subtract": calculator.subtract,
    "multiply": calculator.multiply,
}

USAGE = """usage:
  python -m app.cli greet <name>
  python -m app.cli add <a> <b>
  python -m app.cli subtract <a> <b>
  python -m app.cli multiply <a> <b>"""


def main() -> None:
    args = sys.argv[1:]

    if len(args) == 2 and args[0] == "greet":
        print(greetings.greet(args[1]))
    elif len(args) == 3 and args[0] in OPERATIONS:
        try:
            a, b = float(args[1]), float(args[2])
        except ValueError:
            print(USAGE)
            raise SystemExit(1)
        print(OPERATIONS[args[0]](a, b))
    else:
        print(USAGE)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
