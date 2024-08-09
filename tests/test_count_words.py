"""
Words words words? words
"""

from .test_base import *
from qje5vf.tokenize_text import tokenize, count_words, clean_text

def test_count_words_french():
    """
    Test the count_words function on a French text.

    This function verifies that count_words correctly returns a dictionary of word counts,
    and checks that specific words like 'corbeau' are counted accurately in the French text.
    """
    word_count = count_words(FRENCH_TEXT)
    # pylint: disable=no-member
    tokenized_words = tokenize(clean_text(FRENCH_TEXT))
    assert isinstance(
        word_count, dict), "Word count did not produce a dictionary"
    assert word_count.get(
        'corbeau') == 1, "Incorrect count for the word 'corbeau'"


@pytest.mark.parametrize("input_text, expected_counts", [
    (
        "the quick brown fox jumps over the lazy dog",
        {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
    ),
    ("to be or not to be", {'to': 2, 'be': 2, 'or': 1, 'not': 1}),
    ("a a a a b b c", {'a': 4, 'b': 2, 'c': 1})
])
def test_count_words_simple(input_text, expected_counts):
    """
    Test the count_words function on simple input strings.

    This function checks if count_words correctly counts the frequency of each word
    and returns the expected dictionary of word counts for various input strings.
    """
    word_counts = count_words(input_text)
    assert word_counts == expected_counts, f"Count words failed for input: {input_text}\nExpected: {expected_counts}\nGot: {word_counts}"


@pytest.mark.parametrize("filename, common_words", [
    ('pg1064.txt', ['the', 'of', 'and', 'to', 'a']),
    ('pg17192.txt', ['the', 'of', 'and', 'to', 'a']),
    ('pg32037.txt', ['the', 'of', 'and', 'to', 'a']),
    ('pg51060.txt', ['the', 'of', 'and', 'to', 'a'])
])
def test_count_words_files(filename, common_words):
    """
    Test the count_words function on content from multiple files.

    This function checks if count_words returns a dictionary where common English words
    (e.g., 'the', 'of', 'and') appear frequently in the content of each file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    word_counts = count_words(content)
    assert isinstance(
        word_counts, dict), f"Count words failed to return a dictionary for {filename}"
    for word in common_words:
        assert word in word_counts, f"'{word}' not found in {filename}"
        assert word_counts[word] > 5, f"'{word}' appears less than 5 times in {filename}"


def test_count_words_basic():
    """
    Test the count_words function on a basic text sample.

    This function verifies that count_words returns a dictionary with accurate word counts
    for common words in the sample text, such as 'the', 'word', and 'raven'.
    """
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word,'
    word_counts = count_words(text)
    assert isinstance(
        word_counts, dict), f"Count words failed to return a dictionary: {word_counts}"
    assert word_counts[
        'raven'] == 1, f"Count words failed to correctly count 'raven': {word_counts['raven']}"


def test_count_words_case_insensitive():
    """
    Test the count_words function for case insensitivity.

    This function checks if count_words correctly treats words with different cases
    (e.g., 'Raven' and 'raven') as the same word in the resulting dictionary.
    """
    text = 'The Raven and the raven are the same Raven'
    word_counts = count_words(text)
    assert word_counts[
        'raven'] == 3, f"Count words failed to be case-insensitive: {word_counts['raven']}"


def test_count_words_punctuation():
    """
    Test the count_words function with a string containing punctuation.

    This function verifies that count_words correctly ignores punctuation and
    counts words accurately, even in the presence of contractions and special characters.
    """
    text = "It's a Raven! What's it doing here? (Nevermore)"
    word_counts = count_words(text)
    assert 'its' in word_counts, "Count words failed to handle contractions correctly"
    assert 'nevermore' in word_counts, "Count words failed to handle parentheses correctly"


def test_count_words_file():
    """
    Test the count_words function on the content of "The Cask of Amontillado" file.

    This function checks if count_words returns a dictionary with accurate word counts
    for the entire content of the file, ensuring that specific words are included.
    """
    with open('pg1063.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    word_counts = count_words(content)
    assert isinstance(
        word_counts, dict), "Count words failed to return a dictionary for file content"
    assert len(
        word_counts) > 100, f"Count words returned few unique words: {len(word_counts)}"
    assert 'amontillado' in word_counts, "Count words failed to include 'amontillado' in counts"


def test_count_words_multiple_files():
    """
    Test the count_words function on combined content from multiple files.

    This function verifies that count_words returns a dictionary with accurate word counts
    """
    files = ['pg17192.txt', 'pg932.txt', 'pg1063.txt', 'pg10031.txt']
    combined_content = ''
    for file in files:
        with open(file, 'r', encoding='utf-8') as file:
            combined_content += file.read()
    word_counts = count_words(combined_content)
    assert isinstance(
        word_counts, dict), "Count words failed to return a dictionary"
    assert len(
        word_counts) > 1000, f"Count words returned few unique words: {len(word_counts)}"
    assert 'raven' in word_counts, "Count words failed to include 'raven' in counts"
    assert 'usher' in word_counts, "Count words failed to include 'usher' in counts"
    assert 'amontillado' in word_counts, "failed include 'amontillado' in counts"


@pytest.mark.xfail(reason="This test is designed to fail")
def test_count_words_fail():
    """
    Test case designed to fail for the count_words function.

    This function checks if count_words incorrectly counts the words 'The' and 'the'
    separately, which is not the expected behavior (case insensitivity should be applied).
    """
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word,'
    word_counts = count_words(text)
    assert word_counts['the'] != word_counts['The'], "unexpectedly combined 'the' and 'The'"
