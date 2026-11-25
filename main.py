#!/usr/bin/env python3
"""One Line, One Laugh -- entry program.

Writes a single funny line to /output/entry.txt.
Eight hand-written candidates, each scored 0-10 on the judge brief's
criteria (laugh, turn, tightness, freshness, clarity), summed;
highest total wins, ties broken by the shorter line, then by order.
Deterministic: no randomness, no network, no input files.
"""

import os

# (line, laugh, turn, tight, fresh, clear)
CANDIDATES = [
    (
        "My smart fridge just emailed me about my midnight snacking, "
        "so now even my leftovers are judging me.",
        7, 7, 7, 6, 9,
    ),
    (
        "I told my plants I was leaving for the weekend; "
        "they all died out of spite before I packed.",
        7, 8, 8, 7, 8,
    ),
    (
        "My therapist says I have a fear of commitment, so I married my "
        "gym membership instead -- at least it never texts back.",
        6, 6, 5, 5, 8,
    ),
    (
        "I asked AI to write my wedding vows; "
        "it proposed to the printer.",
        8, 9, 9, 8, 9,
    ),
    (
        "My password is so strong even I can't log in, which makes it "
        "the most secure account nobody owns.",
        8, 8, 8, 7, 9,
    ),
    (
        "I bought a standing desk to be healthier; "
        "now I just sit on the floor next to it.",
        7, 8, 9, 7, 9,
    ),
    (
        "My dog ate my homework, then filed a complaint "
        "about the seasoning.",
        8, 8, 8, 6, 9,
    ),
    (
        "I tried to meditate, but my brain opened twelve tabs "
        "and started arguing with itself.",
        7, 7, 6, 6, 8,
    ),
]


def score(candidate):
    line, laugh, turn, tight, fresh, clear = candidate
    return laugh + turn + tight + fresh + clear


def pick(candidates):
    """Highest total wins; ties go to the shorter line, then earliest."""
    best = None
    best_key = None
    for candidate in candidates:
        key = (score(candidate), -len(candidate[0]))
        if best_key is None or key > best_key:
            best = candidate
            best_key = key
    return best


def audit_output(path, expected_line):
    """Re-read the written file and verify it byte for byte.

    Checks: byte length matches the line's UTF-8 encoding, the
    checksum (sum of bytes mod 9973) matches, and the first and last
    characters anchor to the expected line's own ends.
    """
    with open(path, "rb") as f:
        raw = f.read()
    expected = expected_line.encode("utf-8")
    assert raw == expected, "written bytes differ from chosen line"
    byte_len = len(raw)
    checksum = sum(raw) % 9973
    first_anchor = raw[:1].decode("utf-8")
    last_anchor = raw[-1:].decode("utf-8")
    assert first_anchor == expected_line[0], "first character mismatch"
    assert last_anchor == expected_line[-1], "last character mismatch"
    return {"bytes": byte_len, "checksum_mod_9973": checksum,
            "first": first_anchor, "last": last_anchor}


def main():
    winner = pick(CANDIDATES)
    line = winner[0]
    assert 1 <= len(line) <= 140, "entry must be 1-140 characters"
    assert line.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod("/output/entry.txt", 0o644)
    report = audit_output("/output/entry.txt", line)
    print("winner score:", score(winner), "chars:", len(line))
    print("audit:", report)


if __name__ == "__main__":
    main()
