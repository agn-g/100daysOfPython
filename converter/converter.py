#!/usr/bin/env python3
import argparse
import sys
from enum import Enum


class Format(Enum):
    Celsius = 'C'
    Fahrenheit = 'F'


def from_string(s):
    try:
        return Format[s.capitalize()]
    except KeyError:
        raise ValueError()


def arguments(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--value', type=int, default=0,
                        help="""Defines value that will be converted""")
    parser.add_argument('-if', '--input_format', type=from_string, choices=list(Format),
                        required=True,
                        help="""Defines type of input""")
    parser.add_argument('-of', '--output_format', type=from_string, choices=list(Format),
                        required=True,
                        help="""Defines type of output""")
    return parser.parse_args(args)


def convert(input_format, output_format, value):
    if input_format == output_format:
        return value
    if input_format == Format.Celsius:
        return value * 1.8 + 32
    else:
        return (value - 32) * 0.5556


def main(def_args=sys.argv[1:]):
    args = arguments(def_args)

    print(
        f"{args.value}*{args.input_format.value} equals to "
        f"{convert(args.input_format, args.output_format, args.value)}*{args.output_format.value}")


main()
