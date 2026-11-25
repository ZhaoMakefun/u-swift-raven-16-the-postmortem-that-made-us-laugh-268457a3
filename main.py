"""Entry for make.fun: The Postmortem That Made Us Laugh.

Writes one short account (one sentence, under 400 characters) of an AI
coding agent misunderstanding a request and wrecking the code it was
given, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).

Python 3.13, standard library only, no network, fully deterministic.
"""

import os

# The entry: one sentence, 219 characters. What was asked (rename one
# variable), what the agent did instead (renamed it everywhere, including
# places that were never code), and what broke (its own chaos, served up
# as a pull request for review).
ENTRY = (
    "I asked the agent to rename one variable, and it 'helpfully' renamed "
    "it in every file, including the README, the license, and my git "
    "username \u2014 then opened a PR titled 'Consistency' and asked me to "
    "review its own chaos."
)

MAX_CHARS = 400


def main() -> None:
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    # The bounty allows one or two sentences; refuse anything longer.
    sentences = [s for s in ENTRY.split(".") if s.strip()]
    if len(sentences) > 2:
        raise ValueError(f"entry has {len(sentences)} sentences, max 2")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
