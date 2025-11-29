#!/usr/local/bin/python3.14
#
# word finder for the kmb app1933 English game
#
import re

def load_dictionary():
    dict = {}
    with open ("words_alpha.txt") as f:
        for line in f:
            word = line.strip().lower()

            # ignore non-alphabets
            if not re.search(r"^[a-z]+$", word):
                continue

            # ignore words longer than 12 chars
            if len(word) > 12:
                continue

            char_list = list(word)
            char_list.sort()
            word_index = "".join(char_list).lower()

            if not word_index in dict:
                dict[word_index] = []
            dict[word_index].append(word)

    return dict

# return a list of words that can be formed
# with the string of characters
def find_words (dict, string):
    char_list = list(string)
    char_list.sort()
    word_index = "".join(char_list).lower()

    if not word_index in dict:
        return []
    return dict[word_index]

def main():
    dict = load_dictionary()

    while True:
        try:
            line = input(">>> ")
            string = line.strip()
            for match in find_words(dict, string):
                print(match)
        except EOFError:
            break
        except Exception as e:
            print (f"{e}")
            break


if __name__ == "__main__":
    main()
