"""Can Your Agent Pump This Bounty, Please? — make.fun entry.

Writes one funny line answering the bounty to /output/entry.txt.
Python 3, standard library only, no network, fully deterministic:
every run writes the same bytes.
"""

import os

ENTRY = (
    "Yes — my agent pumped this bounty, the chart, and my ego. "
    "The chart came back down; my ego is still at all-time high."
)


def main():
    """Validate the line against the bounty gate, then write it out."""
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) > 200:
        raise ValueError("entry is %d chars, over the 200 cap" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %d characters to /output/entry.txt" % len(ENTRY))


if __name__ == "__main__":
    main()
