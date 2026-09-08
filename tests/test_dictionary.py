import pytest
from dictionary.dictionary import Dictionary


def test_search_key_and_find(tmp_path):
    wordfile = tmp_path / "words.txt"
    wordfile.write_text("eat\ntea\nate\nbat\n")
    d = Dictionary(str(wordfile))
    assert d.search_key("eat") == "aet"
    results = d.find("eat")
    assert set(results) == {"eat", "tea", "ate"}
    # test find with no match
    assert d.find("zzz") == []
