import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')));

import pytest
from tokenize_text import tokenize, clean_text
from tests.expected_failure_decorator import expected_to_fail




@pytest.mark.parametrize("input_text, expected_count", [
    ("The quick brown fox", 4),
    ("jumps over the lazy dog", 5),
    ("Hello, World!", 2),
    ("   Extra   spaces   ", 2),
    ("", 0),
])
def test_tokenize_count(input_text, expected_count):
    # Given various input strings
    # When I pass each string to the tokenize() function
    # Then I should get the expected number of tokens
    tokens = tokenize(input_text)
    assert len(tokens) == expected_count, f"Tokenize failed for input: {input_text}\nExpected count: {expected_count}\nGot: {len(tokens)}"






@pytest.mark.parametrize("filename", [
    'pg1064.txt',
    'pg17192.txt',
    'pg32037.txt',
    'pg51060.txt'
])
def test_tokenize_files(filename):
    # Given content from multiple files
    # When I pass the content of each file to the tokenize() function
    # Then I should get a non-empty list of tokens
    with open(filename, 'r') as file:
        content = file.read()
    tokens = tokenize(content)
    assert isinstance(tokens, list), f"Tokenize failed to return a list for {filename}"
    assert len(tokens) > 0, f"Tokenize returned an empty list for {filename}"


def test_tokenize_basic():
    # Given a cleaned string of text
    # When I pass the string to the tokenize() function
    # Then I should get a list of words
    text = 'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour'
    tokens = tokenize(text)
    assert isinstance(tokens, list), f"Tokenize failed to return a list: {tokens}"
    assert len(tokens) == 25, f"Tokenize failed to correctly split words: {tokens}"

def test_tokenize_single_word():
    # Given a single word
    # When I pass the word to the tokenize() function
    # Then I should get a list with one item
    text = 'nevermore'
    tokens = tokenize(text)
    assert tokens == ['nevermore'], f"Tokenize failed on single word: {tokens}"

def test_tokenize_empty_string():
    # Given an empty string
    # When I pass the empty string to the tokenize() function
    # Then I should get an empty list
    text = ''
    tokens = tokenize(text)
    assert tokens == [], f"Tokenize failed on empty string: {tokens}"

def test_tokenize_file():
    # Given the content of "The Fall of the House of Usher" file
    # When I pass the cleaned content to the tokenize() function
    # Then I should get a list of words
    with open('pg932.txt', 'r') as file:
        content = file.read()
    cleaned = clean_text(content)
    tokens = tokenize(cleaned)
    assert isinstance(tokens, list), "Tokenize failed to return a list for file content"
    assert len(tokens) > 1000, f"Tokenize returned unexpectedly few tokens: {len(tokens)}"
    assert 'usher' in tokens, "Tokenize failed to include 'usher' in tokens"

def test_tokenize_french():
    # Given the content of the French "Le Corbeau" file
    # When I pass the cleaned content to the tokenize() function
    # Then I should get a list of words including French words
    with open('pg14082.txt', 'r') as file:
        content = file.read()
    cleaned = clean_text(content)
    tokens = tokenize(cleaned)
    assert isinstance(tokens, list), "Tokenize failed to return a list for French content"
    assert 'corbeau' in tokens, "Tokenize failed to include 'corbeau' in French tokens"
    assert any('é' in word for word in tokens), "Tokenize failed to preserve accented characters"

@expected_to_fail
def test_tokenize_fail():
    # Given a string of text
    # When I pass the string to the tokenize() function
    # Then I expect it to return a single string (which it shouldn't)
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    tokens = tokenize(text)
    assert isinstance(tokens, str), "Tokenize unexpectedly returned a non-string type"
