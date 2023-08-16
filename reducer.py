#!/usr/bin/env python3

import sys

def main():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        word, count = line.strip().split('\t', 1)
        count = int(count)

        if current_word == word:
            current_count += count
        else:
            if current_word:
                print(f"{current_word}\t{current_count}")
            current_word, current_count = word, count

    if current_word == word:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    main()
