from gencontent import extract_title
import pytest

def test_extract_title():
    md = "# This is a header"
    assert extract_title(md) == "This is a header"

def test_extract_title_raises():
    md = "This is just some text.\nI know I am so creative."
    with pytest.raises(Exception):
        extract_title(md)
