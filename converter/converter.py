#!/usr/bin/env python3
import argparse
import sys


def arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--value', type=int, default=0,
                        help="""Defines value that will be converted""")
    return parser.parse_args(args)


def convert(input_format, output_format, value):
    if input_format == output_format:
        return value
    if input_format == 'C':
        return value * 1.8 + 32
    else:
        return (value - 32) * 0.5556


def main(def_args=sys.argv[1:]):
    args = arguments(def_args)
    print(f"{args.value}*C equals to {convert('C', 'F', args.value)}*F")
    print(f"{args.value}*F equals to {convert('F', 'C', args.value)}*C")


main()
