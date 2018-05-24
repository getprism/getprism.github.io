#!/usr/bin/env python3

import os.path
import shutil

BASE_DIR = os.path.join(
    os.path.expanduser('~'),
    'Documents/Projects/Prism/fastlane/screenshots/en-AU'
)

SCREENSHOTS = [
    ('iPhone 8-00_player_dark.png', 'player.png'),
    ('iPhone 8-01_libraries.png', 'access.png'),
    ('iPhone 8-02_filters.png', 'filters.png'),
    ('iPhone 8-03_display.png', 'arrange.png'),
    ('iPhone 8-04_list.png', 'list.png'),
]


def main():
    for src, dst in SCREENSHOTS:
        shutil.copy2(
            os.path.join(BASE_DIR, src),
            os.path.join('.', dst)
        )


if __name__ == '__main__':
    main()
