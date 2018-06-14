#!/usr/bin/env python3

import os.path
import shutil

BASE_DIR = os.path.join(
    os.path.expanduser('~'),
    'Documents/Projects/Prism/fastlane/screenshots/en-AU'
)

SCREENSHOTS = [
    ('iPhone 8-00_player_dark.png', 'black/iphone-player.png'),
    ('iPhone 8-01_libraries.png', 'silver/iphone-access.png'),
    ('iPhone 8-02_filters.png', 'silver/iphone-filters.png'),
    ('iPhone 8-03_display.png', 'silver/iphone-arrange.png'),
    ('iPhone 8-04_list.png', 'silver/iphone-list.png'),

    ('iPad Pro (9.7-inch)-00_player_dark.png', 'black/ipad-player.png'),
#    ('iPad Pro (9.7-inch)-01_libraries.png', 'silver/ipad-access.png'),
#    ('iPad Pro (9.7-inch)-02_filters.png', 'silver/ipad-filters.png'),
#    ('iPad Pro (9.7-inch)-03_display.png', 'silver/ipad-arrange.png'),
#    ('iPad Pro (9.7-inch)-04_list.png', 'silver/ipad-list.png'),
]


def main():
    for src, dst in SCREENSHOTS:
        shutil.copy2(
            os.path.join(BASE_DIR, src),
            os.path.join('.', dst)
        )


if __name__ == '__main__':
    main()
