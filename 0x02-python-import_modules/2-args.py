#!/usr/bin/python3
import sys

def printCmdArgvs():
    args = sys.argv[1:]
    num_args = len(args)
    
    if num_args == 0:
        print(f"{num_args} arguments.")
    elif num_args == 1:
        print(f"{num_args} argument:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")
    else:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    printCmdArgvs()


