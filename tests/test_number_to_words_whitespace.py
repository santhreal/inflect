import inflect


def test_whitespace_only_number_to_words():
    p = inflect.engine()
    for text in (" ", "  ", "\t", "\n", "\r"):
        assert p.number_to_words(text) == "zero"


def test_signed_numbers_unchanged():
    p = inflect.engine()
    assert p.number_to_words("-1") == "minus one"
    assert p.number_to_words("+2") == "plus two"
