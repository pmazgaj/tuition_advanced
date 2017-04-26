"""
Rename files name, for catalogs (order, structure, etc.).
"""
import os
import sys


def find_file(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed path checking BEFORE changing words in function {}".format(original_function.__name__))
        return original_function(*args, **kwargs)

    return wrapper_function


def switch_orders(path, name):
    print("path: {} name: {}".format(path, name))


def result():
    switch_order()
    switch_orders("aa", "cc")


result()
