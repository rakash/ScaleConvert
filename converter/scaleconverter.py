### https://realpython.com/pypi-publish-python-package/
## if you need a package that should be executable like "python converter" then there should be a __main__.py file. read the above article.

import sys

def celsius_to_fahrenheit(n):
    """
    celsius to fahrenheit
    """
    try:
        f = (n * 1.8) + 32
        return f
    except TypeError:
        n = "Enter a number"
        return n

def fahrenheit_to_celcius(n):
    """
    fahrenheit to celsius
    """
    try:
        c = (n - 32) / 1.8
        return c
    except TypeError:
        n = "Enter a number"
        return n

def add_temp_scales(n):
    a = fahrenheit_to_celcius(n)
    b = celsius_to_fahrenheit(n)
    result = a + b
    return result

def subtract_temp_scales(n):
    a = fahrenheit_to_celcius(n)
    b = celsius_to_fahrenheit(n)
    result = a - b
    return result
    
def inr_to_usd(vals):
    try:
        value = vals * 0.012
        return value
    except Exception as e:
        print(e)
        return "Enter a valid value"


