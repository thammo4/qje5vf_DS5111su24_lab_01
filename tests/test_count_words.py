import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')));

import pytest
from tokenize_text import tokenize, count_words, clean_text
from tests.expected_failure_decorator import expected_to_fail

french_text="_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"

def test_count_words_french():
    tokenized_words = tokenize(clean_text(french_text))
    word_count = count_words(french_text)
    assert isinstance(word_count, dict), "Word count did not produce a dictionary"
    assert word_count.get('corbeau') == 1, "Incorrect count for the word 'corbeau'"

@pytest.mark.parametrize("input_text, expected_counts", [
    ("the quick brown fox jumps over the lazy dog", {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}),
    ("to be or not to be", {'to': 2, 'be': 2, 'or': 1, 'not': 1}),
    ("a a a a b b c", {'a': 4, 'b': 2, 'c': 1})
])
def test_count_words_simple(input_text, expected_counts):
    # Given a simple input string
    # When I pass the string to the count_words() function
    # Then I should get a dictionary with the expected word counts
    word_counts = count_words(input_text)
    assert word_counts == expected_counts, f"Count words failed for input: {input_text}\nExpected: {expected_counts}\nGot: {word_counts}"

@pytest.mark.parametrize("filename, common_words", [
    ('pg1064.txt', ['the', 'of', 'and', 'to', 'a']),
    ('pg17192.txt', ['the', 'of', 'and', 'to', 'a']),
    ('pg32037.txt', ['the', 'of', 'and', 'to', 'a']),
    ('pg51060.txt', ['the', 'of', 'and', 'to', 'a'])
])
def test_count_words_files(filename, common_words):
    # Given the content of a file
    # When I pass the content to the count_words() function
    # Then I should get a dictionary with common English words appearing frequently
    with open(filename, 'r') as file:
        content = file.read()
    word_counts = count_words(content)
    assert isinstance(word_counts, dict), f"Count words failed to return a dictionary for {filename}"
    for word in common_words:
        assert word in word_counts, f"Common word '{word}' not found in {filename}"
        assert word_counts[word] > 5, f"Common word '{word}' appears less than 5 times in {filename}"












def test_count_words_basic():
    # Given a string of text
    # When I pass the string to the count_words() function
    # Then I should get a dictionary with word counts
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    word_counts = count_words(text)
    assert isinstance(word_counts, dict), f"Count words failed to return a dictionary: {word_counts}"
    assert word_counts['the'] == 2, f"Count words failed to correctly count 'the': {word_counts['the']}"
    assert word_counts['word'] == 2, f"Count words failed to correctly count 'word': {word_counts['word']}"
    assert word_counts['raven'] == 1, f"Count words failed to correctly count 'raven': {word_counts['raven']}"

def test_count_words_case_insensitive():
    # Given a string with mixed case words
    # When I pass the string to the count_words() function
    # Then I should get a dictionary with case-insensitive word counts
    text = 'The Raven and the raven are the same Raven'
    word_counts = count_words(text)
    assert word_counts['raven'] == 3, f"Count words failed to be case-insensitive: {word_counts['raven']}"

def test_count_words_punctuation():
    # Given a string with punctuation
    # When I pass the string to the count_words() function
    # Then I should get a dictionary with word counts ignoring punctuation
    text = "It's a Raven! What's it doing here? (Nevermore)"
    word_counts = count_words(text)
    assert 'its' in word_counts, "Count words failed to handle contractions correctly"
    assert 'nevermore' in word_counts, "Count words failed to handle parentheses correctly"

def test_count_words_file():
    # Given the content of "The Cask of Amontillado" file
    # When I pass the content to the count_words() function
    # Then I should get a dictionary with word counts for the entire file
    with open('pg1063.txt', 'r') as file:
        content = file.read()
    word_counts = count_words(content)
    assert isinstance(word_counts, dict), "Count words failed to return a dictionary for file content"
    assert len(word_counts) > 100, f"Count words returned unexpectedly few unique words: {len(word_counts)}"
    assert 'amontillado' in word_counts, "Count words failed to include 'amontillado' in counts"

def test_count_words_multiple_files():
    # Given the content of multiple files
    # When I pass the combined content to the count_words() function
    # Then I should get a dictionary with word counts for all files
    files = ['pg17192.txt', 'pg932.txt', 'pg1063.txt', 'pg10031.txt']
    combined_content = ''
    for file in files:
        with open(file, 'r') as f:
            combined_content += f.read()
    word_counts = count_words(combined_content)
    assert isinstance(word_counts, dict), "Count words failed to return a dictionary for multiple files"
    assert len(word_counts) > 1000, f"Count words returned unexpectedly few unique words for multiple files: {len(word_counts)}"
    assert 'raven' in word_counts, "Count words failed to include 'raven' in counts for multiple files"
    assert 'usher' in word_counts, "Count words failed to include 'usher' in counts for multiple files"
    assert 'amontillado' in word_counts, "Count words failed to include 'amontillado' in counts for multiple files"

@pytest.mark.xfail(reason="This test is designed to fail")
def test_count_words_fail():
    # Given a string with mixed case words
    # When I pass the string to the count_words() function
    # Then I expect it to count 'The' and 'the' separately (which it shouldn't)
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    word_counts = count_words(text)
    assert word_counts['the'] != word_counts['The'], "Count words unexpectedly combined 'the' and 'The'"
