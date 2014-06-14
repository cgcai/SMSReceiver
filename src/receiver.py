#!/usr/env/bin python
import argparse
import os


def main(args):
    pass


if __name__ == '__main__':
    parser = new ArgumentParser()
    parser.add_argument('--tty', type=str, required=True, help='tty of the '
                        'USB Modem.')
    args = parser.parse_args()

    # Normalize file path.
    args.tty = os.path.abspath(args.tty)

    main(args)
