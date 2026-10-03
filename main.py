"""InZOI Desktop — A local helper for InZOI city folders, household files, and Canvas Studio exports."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='inzoi_desktop',
        description='A local helper for InZOI city folders, household files, and Canvas Studio exports.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('InZOI Desktop')
    print('Keep families on disk before a realism patch.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
