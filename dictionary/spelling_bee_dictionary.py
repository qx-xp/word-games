import re
from .dictionary import Dictionary

class SpellingBeeDictionary(Dictionary):
    default_wordfile = "words_alpha.txt"

    def __init__(self, chars, wordfile=default_wordfile):
        self.chars = chars
        self.char_matcher = re.compile(fr"^[{re.escape(chars)}]+$", re.IGNORECASE)

        super().__init__(wordfile)
        

    # only include words that can be formed by the spelling bee chars
    def is_valid(self, word):
        # word must be at least 3 letters long
        if len(word) < 3:
            return False

        return self.char_matcher.search(word)

    # dictionary key is the unique sorted characters of a word
    def search_key(self, word):
        char_list = list(set(word.lower()))
        char_list.sort()
        return "".join(char_list)


    def load(self, wordfile):
        dict = {}
        with open (wordfile) as f:
            for line in f:
                word = line.strip().lower()

                if not self.is_valid(word):
                    continue

                key = self.search_key(word)

                if not key in dict:
                    dict[key] = []
                dict[key].append(word)

        return dict
