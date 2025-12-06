import re
from .dictionary import Dictionary

class KMBDictionary(Dictionary):
    default_wordfile = "words_kmb.txt"
    def __init__(self, wordfile=default_wordfile):
        super().__init__(wordfile)

    # skip words longer than 12 chars
    # and words with non-alphabets
    def can_skip(self, word):
        # skip words with non-alphabets
        if not re.search(r"^[a-z]+$", word):
            return True

        # skip words longer than 12 chars
        if len(word) > 12:
            return True

        return False
