#!/usr/bin/env python3

"""
Display terminal color scheme.

"""

import argparse
from rich.console import Console
from rich.table import Table


def get_row_args(num: int, color: str, code: int, text: str, bold: bool = False) -> list:
    """
    Generate arguments for color row.

    """

    if bold:
        code = f'1;{code}'
        color = f'bold {color}'

    args = [f'{code}m']

    for i in range(num):
        args.append(f'[{color}] {text} [/{color}]')

    return args


def print_palette(text: str, bold: bool = True) -> None:
    """
    Print colors.

    """

    colors = {
        'default': 39,
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37
    }

    table = Table(box=None)

    table.add_column('', justify='right')

    for c, v in colors.items():
        table.add_column(f'{v + 10}m', justify='center', style=f'default on {c}')

    for c, v in colors.items():
        table.add_row(*get_row_args(len(colors), c, v, text))

        if bold:
            table.add_row(*get_row_args(len(colors), c, v, text, bold=True))

    print()
    console = Console()
    console.print(table)
    print()
    print('View link below for hex codes for this color scheme:')
    print('https://github.com/gruvbox-community/gruvbox-contrib/blob/master/color.table')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Display terminal color scheme.')

    parser.add_argument(
        '-b',
        dest='bold',
        action='store_true',
        help='Include bold text (default: False)'
    )

    parser.add_argument(
        '-t',
        dest='text',
        default='xYz',
        help='Use custom text instead of default (default: xYz)'
    )

    args = parser.parse_args()

    print_palette(args.text, bold=args.bold)
