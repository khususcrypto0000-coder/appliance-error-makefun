#!/usr/bin/env python3
"""Entry for make.fun bounty: The Funniest Honest Appliance Error.

Writes a single deadpan error line from a tired air fryer to
/output/entry.txt. Standard library only, fully deterministic.
"""

ENTRY = (
    "Error: basket removed 14 times to check the fries. "
    "They were not ready then. They are not ready now. "
    "Please close the drawer and let me work."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
