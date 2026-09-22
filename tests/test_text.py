from utils.text_utils import clean_text


def test_clean_text_removes_nulls_and_normalizes_spacing():
    text = "hello\x00   world\n\n\nthis\n is   a test"
    cleaned = clean_text(text)
    assert "\x00" not in cleaned
    assert "hello world" in cleaned
    assert "this is a test" in cleaned
