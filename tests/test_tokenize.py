"""
johnny b goode
"""

from .test_base import *
from qje5vf.tokenize_text import tokenize, clean_text

@pytest.mark.parametrize("input_text, expected_count", [
    ("The quick brown fox", 4),
    ("jumps over the lazy dog", 5),
    ("Hello, World!", 2),
    ("   Extra   spaces   ", 2),
    ("", 0),
])
def test_tokenize_count(input_text, expected_count):
    """
    Test the tokenize function for counting tokens in various input strings.

    This function checks whether the number of tokens returned by tokenize()
    matches the expected count for different input strings, including cases
    with punctuation, extra spaces, and empty strings.
    """
    tokens = tokenize(input_text)
    assert len(
        tokens) == expected_count, f"Tokenize failed for input: {input_text}\nExpected count: {expected_count}\nGot: {len(tokens)}"


@pytest.mark.parametrize("filename", [
    'pg1064.txt',
    'pg17192.txt',
    'pg32037.txt',
    'pg51060.txt'
])
def test_tokenize_files(filename):
    """
    Test the tokenize function on the contents of multiple text files.

    This function checks if the tokenize() function returns a non-empty list
    of tokens when applied to the content of each file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    tokens = tokenize(content)
    assert isinstance(
        tokens, list), f"Tokenize failed to return a list for {filename}"
    assert len(tokens) > 0, f"Tokenize returned an empty list for {filename}"


def test_tokenize_basic():
    """
    Test the tokenize function on a basic cleaned string of text.

    This function checks if the tokenize() function correctly splits the text
    into a list of words, ensuring the correct number of tokens is returned.
    """
    text = 'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour'
    tokens = tokenize(text)
    assert isinstance(
        tokens, list), f"Tokenize failed to return a list: {tokens}"
    assert len(
        tokens) == 25, f"Tokenize failed to correctly split words: {tokens}"


def test_tokenize_single_word():
    """
    Test the tokenize function on a single word.

    This function checks if the tokenize() function returns a list containing
    just the single word.
    """
    text = 'nevermore'
    tokens = tokenize(text)
    assert tokens == ['nevermore'], f"Tokenize failed on single word: {tokens}"


def test_tokenize_empty_string():
    """
    Test the tokenize function on an empty string.

    This function checks if the tokenize() function correctly returns an empty
    list when an empty string is provided as input.
    """
    text = ''
    tokens = tokenize(text)
    assert tokens == [], f"Tokenize failed on empty string: {tokens}"


def test_tokenize_file():
    """
    Test the tokenize function on the content of "The Fall of the House of Usher" file.

    This function checks if the tokenize() function returns a list of words
    when given the cleaned content of the file, ensuring that specific words
    are included and that the list has a reasonable number of tokens.
    """
    with open('pg932.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned = clean_text(content)
    tokens = tokenize(cleaned)
    assert isinstance(
        tokens, list), "Tokenize failed to return a list for file content"
    assert len(
        tokens) > 1000, f"Tokenize returned unexpectedly few tokens: {len(tokens)}"
    assert 'usher' in tokens, "Tokenize failed to include 'usher' in tokens"


def test_tokenize_french():
    """
    Test the tokenize function on the content of a French text file.

    This function checks if the tokenize() function returns a list of words
    when given the cleaned content of the file, ensuring that French words
    and accented characters are preserved in the tokens.
    """
    with open('pg14082.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned = clean_text(content)
    tokens = tokenize(cleaned)
    assert isinstance(
        tokens, list), "Tokenize failed to return a list for French content"
    assert 'corbeau' in tokens, "Tokenize failed to include 'corbeau' in French tokens"
    assert any(
        'é' in word for word in tokens), "Tokenize failed to preserve accented characters"


@expected_to_fail
def test_tokenize_fail():
    """
    Test case designed to fail for the tokenize function.

    This function checks if the tokenize() function incorrectly returns a single
    string instead of a list of tokens, which is not the expected behavior.
    """
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    tokens = tokenize(text)
    assert isinstance(
        tokens, str), "Tokenize unexpectedly returned a non-string type"
