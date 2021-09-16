#!/usr/bin/env python3

def convert(input_format, output_format, value):
    if input_format == output_format:
        return value
    if input_format == 'C':
        return value * 1.8 + 32
    else:
        return (value - 32) * 0.5556


celsius = int(input('Enter temperature in Celsius: '))
fahrenheit = convert('C', 'F', celsius)
print(f'{celsius}*C equals to {fahrenheit}*F')

fahrenheit = int(input('Enter temperature in Fahrenheit: '))
celsius = convert('F', 'C', fahrenheit)
print(f'{fahrenheit}*C equals to {celsius}*F')
