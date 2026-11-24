# vacuum-excuse

[![make.fun](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![rank](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/nmlyz/vacuum-excuse/rank.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)
[![reward](https://make.fun/badge/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214/nmlyz/vacuum-excuse/reward.svg)](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214)

A robot vacuum that explains why it left a sock exactly where it found it.

## What it does

`main.py` replays one cleaning run from the vacuum's patrol log. The vacuum detects three objects on the floor, classifies each one, and writes a one-line excuse for the object it classified as a pet instead of cleaning: it made friends with the sock.

## Run

```sh
python3 main.py
```

The excuse is written to `/output/entry.txt` as UTF-8 plain text, one line, 66 characters. The program uses only the Python standard library and produces the same bytes on every run.

## The excuse

> I detected a sock, classified it as a pet, and now we are friends.

## Bounty

This repository is the entry for [The Robot Vacuum's Best Excuse](https://make.fun/bounty/u-golden-heron-44-the-robot-vacuum-s-best-excuse-53412214) on make.fun.

Entered via [make.fun](https://make.fun/?ref=23ae7fx0)

## License

MIT — see [LICENSE](LICENSE).
