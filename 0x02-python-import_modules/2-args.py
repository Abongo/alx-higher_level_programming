#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    arg_word = "arguments" if num_args != 1 else "argument"
    ending = ":" if num_args > 0 else "."

    print("{:d} {}{}{}".format(num_args, arg_word, "", ending))

    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, argv[i]))
