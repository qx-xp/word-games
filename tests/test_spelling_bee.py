from dictionary.spelling_bee_dictionary import SpellingBeeDictionary


def test_is_dictionary_word():
    assert not SpellingBeeDictionary.is_dictionary_word("cat")  # length 3
    assert not SpellingBeeDictionary.is_dictionary_word("abcdefgh")  # >7 unique
    assert SpellingBeeDictionary.is_dictionary_word("word")  # 4 letters


def test_pangram_key_and_is_pangram(tmp_path):
    wordfile = tmp_path / "words.txt"
    # include a pangram and another word
    wordfile.write_text("abcdefg\nsomeother\n")
    solution = tmp_path / "solution.txt"
    sb = SpellingBeeDictionary("abcdefg", wordfile=str(wordfile), solution_file=str(solution))
    assert sb.pangram_search_key("gfedcba") == "abcdefg"
    assert sb.is_pangram("abcdefg")
    assert sb.index_key("wolf") == "wo4"
