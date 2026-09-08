from dictionary.dictionary_updater import DictionaryUpdater


def test_load_and_save(tmp_path):
    wf = tmp_path / "wf.txt"
    wf.write_text("b\nc\na\na\n")
    du = DictionaryUpdater(str(wf))
    assert set(du.dict) == {"a", "b", "c"}
    du.save()
    content = wf.read_text().splitlines()
    assert content == ["a", "b", "c"]
