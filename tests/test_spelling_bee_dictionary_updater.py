from dictionary.spelling_bee_dictionary_updater import SpellingBeeDictionaryUpdater


def test_load_changes(tmp_path):
    wf = tmp_path / "wf.txt"
    wf.write_text("word\nold\n")
    updater = SpellingBeeDictionaryUpdater(str(wf))
    changefile = tmp_path / "changes.txt"
    changefile.write_text("++ newword\n-- old\ninvalid\n++ too\n")
    adds, removes = updater.load_changes(str(changefile))
    assert "newword" in adds
    assert "old" in removes
    # 'too' has 3 letters, should be excluded by is_dictionary_word and not added
    assert "too" not in adds
