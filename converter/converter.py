#!/usr/bin/env python3

celsius = int(input('Enter temperature in Celsius: '))
fahrenheit = celsius * 1.8 + 32
print(f'{celsius}*C equals to {fahrenheit}*F')

fahrenheit = int(input('Enter temperature in Fahrenheit: '))
celsius = (fahrenheit - 32) * 0.5556
print(f'{fahrenheit}*C equals to {celsius}*F')