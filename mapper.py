#!/usr/bin/env python3

import sys

def tokenize(text):
    return text.split()

def main():
    for line in sys.stdin:
        line = line.strip()
        tokens = tokenize(line)
        for token in tokens:
            print(f"{token}\t1")

if __name__ == "__main__":
    main()
