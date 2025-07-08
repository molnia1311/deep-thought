#!/usr/bin/env python3
"""Deep Thought — stdin *or* argv → OpenAI summariser.

Run either of these:
    echo "lots of text" | python app.py
    python app.py lots of text to summarise

If one or more command‑line arguments are supplied, they are joined with
spaces and used as the input; otherwise the program falls back to reading
all of STDIN. The text is sent to OpenAI Chat Completions with a configurable
system prompt (default: "summarize the input in one line") and the single‑line
summary is printed to STDOUT.

Environment variables
---------------------
OPENAI_API_KEY         (required) Your OpenAI API key.
OPENAI_MODEL           (optional) Model name, default ``gpt-4o-mini``.
OPENAI_SYSTEM_PROMPT   (optional) System prompt, default
                       "summarize the input in one line".
"""
from __future__ import annotations

import os
import sys
from typing import List

from openai import OpenAI

# --- Configuration -----------------------------------------------------------
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv(
    "OPENAI_SYSTEM_PROMPT", "summarize the input in one line"
)

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])  # raises KeyError if missing


def gather_input(argv: List[str]) -> str:
    """Return text from argv if present, else from STDIN."""
    if len(argv) > 1:  # argv[0] is script name
        return " ".join(argv[1:]).strip()
    return sys.stdin.read().strip()


def main() -> None:
    text = gather_input(sys.argv)
    if not text:
        return  # Nothing to summarise

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": text},
        ],
        temperature=0.3,
        max_tokens=50,
    )

    summary = response.choices[0].message.content.strip()
    print(summary, flush=True)


if __name__ == "__main__":  # pragma: no cover
    main()

