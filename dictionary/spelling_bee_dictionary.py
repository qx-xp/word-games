import re
from .dictionary import Dictionary

class SpellingBeeDictionary(Dictionary):
    default_wordfile = "words_bee.txt"
    default_solution_file = "bee-solution.txt"

    def __init__(self, chars, wordfile=default_wordfile, solution_file=default_solution_file):
        # first letter is required
        self.required_letter = chars[0]

        # order the chars to match for pangrams
        self.pangram_key = self.pangram_search_key(chars)

        # regex matches if a word only contains the specified chars
        self.letter_matcher = re.compile(fr"^[{re.escape(chars)}]+$", re.IGNORECASE)

        # output the matched words for review
        self.solution_file = solution_file

        super().__init__(wordfile)

    # requirements of a spelling bee word
    @classmethod
    def is_dictionary_word(cls, word):
        # words must be 4 letters or longer
        if len(word) < 4:
            return False

        # spelling bee only uses 7 unique characters
        if len(set(word)) > 7:
            return False

        return True

    # test for solution word
    def is_solution_word(self, word):
        # word must contain the required letter
        if self.required_letter not in word:
            return False

        if not SpellingBeeDictionary.is_dictionary_word(word):
            return False

        # only include words that can be formed by the puzzle's letters
        return self.letter_matcher.search(word)


    # test if a given word is a pangram
    def is_pangram(self, word):
        return self.pangram_search_key(word) == self.pangram_key


    # search for pangram by the unique sorted characters
    def pangram_search_key(self, chars):
        pangram_char_list = list(set(chars.lower()))
        pangram_char_list.sort()
        return "".join(pangram_char_list)


    # return the list of pangrams
    def pangrams(self):
        return self.dict["__PANGRAM__"]

    # dictionary key is the first 2 characters + length of the word
    # e.g. wolf => wo4
    def index_key(self, word):
        return f"{"".join(list(word)[0:2])}{len(word)}"

    def load(self, wordfile):
        dict = {
            "__PANGRAM__": []
        }
        with open(self.solution_file, "w") as out, \
             open(wordfile) as f:

            for line in f:
                word = line.strip().lower()

                if not self.is_solution_word(word):
                    continue

                # write to solution file
                out.write(f'{word}\n')

                # add the word to the dictionary
                key = self.index_key(word)
                if not key in dict:
                    dict[key] = []
                dict[key].append(word)

                # keep a list of pangrams
                if self.is_pangram(word):
                    dict["__PANGRAM__"].append(word)

        return dict

    def find(self, key):
        if not key in self.dict:
            return []
        return self.dict[key]
