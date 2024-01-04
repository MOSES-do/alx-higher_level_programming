#!/usr/bin/python3
import sys


def printCmdArgvs():
    sum = 0
    args = sys.argv[1:]
    for i, arg in enumerate(args, start=1):
        sum += int(arg)

    print(f"{sum}")


if __name__ == "__main__":
    printCmdArgvs()
