#!/usr/bin/python3

"""this defines a text-file reading function"""


def read_file(filename=""):
    """Read and print text from file"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line)

