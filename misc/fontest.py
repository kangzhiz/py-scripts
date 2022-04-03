#!/usr/bin/env python3

"""
Display a block of text to test monospaced fonts.

"""

import argparse


def display_text(italic: bool = False) -> None:
    """
    Print out text block.

    """

    text = """
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    abcdefghijklmnopqrstuvwxyz
    1234567890 !@#$%^&* <=<>=>
    ~~==__--++ :; "'` ,. ? \|/
    B80O9 LIil17 5Ss2Zz ({[]})
    """

    if italic:
        print('\033[3m' + text + '\033[0m')
    else:
        print(text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display a block of text to test monospaced fonts.')

    parser.add_argument(
        '-i',
        dest='italic',
        action='store_true',
        help='Print text in italics (default: False)'
    )

    args = parser.parse_args()

    display_text(args.italic)
