#!/usr/local/bin/python3.14
#
# word finder for NY Times Spelling Bee Game
#

import re
import sys
from dictionary.spelling_bee_dictionary import SpellingBeeDictionary

expected_input = re.compile("^[a-z]{7}$", re.IGNORECASE)

def is_valid_input(chars):
    uniq_char_list = list(set(chars.lower()))
    uniq_char_list.sort()
    uniq_chars = "".join(uniq_char_list)

    return expected_input.match(uniq_chars)

def main():
    while True:
        try:
            line = input("Spelling Bee: Enter the required letter first, followed by 6 optional letters >>> ")
            string = line.strip()
            if is_valid_input(string):
                break
            print("Input should be 7 unique letters. Please try again.")
        except EOFError:
            sys.exit(1)
        except Exception as e:
            print (f"{e}")
            sys.exit(1)

    dict = SpellingBeeDictionary(string)

    # print all pangrams
    print("PANGRAMS:")
    for word in dict.pangrams():
        print(word)
    print()

    # interactive mode
    print("Spelling Bee: Interactive Hint Lookup")
    print("Enter the first 2 chars and the length of the word e.g. wo4")
    while True:
        try:
            line = input(">>> ")
            hint = line.strip()
            for match in dict.find(hint):
                print(match)
        except EOFError:
            break
        except Exception as e:
            print (f"{e}")
            break


if __name__ == "__main__":
    main()
