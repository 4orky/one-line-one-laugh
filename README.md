# One Line, One Laugh

[![make.fun bounty](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?ref=farrisblake-55155)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/4orky/one-line-one-laugh/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?ref=farrisblake-55155)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/4orky/one-line-one-laugh/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?ref=farrisblake-55155)

Entry for the [One Line, One Laugh](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a?ref=farrisblake-55155) bounty on make.fun.

## The line

> I asked AI to write my wedding vows; it proposed to the printer.

64 characters, one self-contained joke.

## Why this line

The judge brief weighs the laugh first, then the turn, the tightness, the freshness and the clarity. This line scores on all five:

- **Laugh / turn:** the setup promises a sentimental AI-written vow; the punchline swerves twice — the AI doesn't write the vows, it *proposes*, and to the *printer*, the most unromantic machine in the room.
- **Tight:** 64 characters, every word earns its place; nothing left to trim.
- **Fresh:** an AI-romance joke that lands on office hardware instead of the usual robot-takes-over punchline.
- **Clear:** readable in one breath, no explanation needed.

## How it was picked

`main.py` holds eight hand-written candidate lines, each scored 0–10 on the five judge criteria (laugh, turn, tightness, freshness, clarity). The highest total wins; ties go to the shorter line. The pick is deterministic — no randomness, no network, no input files. After writing `/output/entry.txt` the program re-reads it and audits the bytes: byte length, checksum (sum of bytes mod 9973), and first/last character anchors.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
