import inflect


def test_whitespace_only_plural_returns_unchanged():
    p = inflect.engine()
    for text in (" ", "  ", "\t", "\r", "\xa0", " \t "):
        assert p.plural(text) == text
        assert p.plural_noun(text) == text
        assert p.singular_noun(text) == text


def test_newline_only_still_unchanged():
    p = inflect.engine()
    assert p.plural("\n") == "\n"
    assert p.plural_noun("\n") == "\n"


def test_leading_trailing_whitespace_still_preserved():
    p = inflect.engine()
    assert p.plural(" ox ") == " oxen "
