#!/usr/bin/env python3
import argparse
import sys
from enum import Enum


class Format(Enum):
    Celsius = "C"
    Fahrenheit = "F"
    Kilometer = "km"
    Mile = 'mi',
    Inch = "in",
    Centimeter = "cm"


def from_string(s):
    try:
        if s.lower() == "mi":
            return Format.Mile
        elif s.lower() == "in":
            return Format.Inch
        else:
            return Format[s.capitalize()]
    except KeyError:
        try:
            return Format(s)
        except ValueError:
            try:
                return Format(s.lower())
            except ValueError:
                raise ValueError()


allowed_conversions: list[tuple[Format, Format]] = [(Format.Celsius, Format.Fahrenheit),
                                                    (Format.Mile, Format.Kilometer),
                                                    (Format.Inch, Format.Centimeter)]


def is_allowed_conversion(input_type, output_type):
    conversion = next(((type1, type2) for (type1, type2) in allowed_conversions
                       if (type1 == input_type and type2 == output_type) or
                       (type1 == output_type and type2 == input_type)), None)
    if conversion is None:
        return False
    else:
        return True


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
    elif input_format == Format.Fahrenheit:
        return (value - 32) * 0.5556
    elif input_format == Format.Kilometer:
        return value * 0.6214
    elif input_format == Format.Centimeter:
        return value * 0.3937
    elif input_format == Format.Inch:
        return value * 2.54
    else:
        return value / 0.6214


def get_unit(format_val):
    if format_val != Format.Celsius and format_val != Format.Fahrenheit:
        if format_val == Format.Mile:
            return 'mi'
        elif format_val == Format.Inch:
            return 'in'
        else:
            return f'{format_val.value}'
    else:
        return f"*{format_val.value}"


def main(def_args=sys.argv[1:]):
    args = arguments(def_args)

    if args.input_format == args.output_format or is_allowed_conversion(args.input_format, args.output_format):
        print(
            f"{args.value} {get_unit(args.input_format)} equals to "
            f"{convert(args.input_format, args.output_format, args.value)} {get_unit(args.output_format)}")
    else:
        print("Unsupported conversion")


main()
