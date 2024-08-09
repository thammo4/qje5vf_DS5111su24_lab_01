"""
    is this not a docstring?
    when you call my name
    it's like a little prayer
"""

import string
from test_base import FRENCH_TEXT

def test_tokenize_french():
    """
    blah blah blah
    """
    cleaned_text = clean_text(FRENCH_TEXT)
    tokenized_words = tokenize(cleaned_text)
    assert isinstance(tokenized_words, list), "Tokenization did not produce a list"
    assert len(tokenized_words) == 69, "Tokenization produced incorrect number of words"
    assert tokenized_words[0] == "mais", "First word in tokenization should be 'mais'"

def clean_text(input_text):
    """
    Cleans the input text by converting it to lowercase and removing punctuation.

    Args:
    input_text (str): The input text to be cleaned.

    Returns:
    str: The cleaned text.
    """
    assert isinstance(input_text, str), "Input should be a string"
    cleaned_text = input_text.lower()
    cleaned_text = cleaned_text.translate(str.maketrans('', '', string.punctuation))
    return cleaned_text

def tokenize(input_text):
    """
    Tokenizes the input text into a list of words.

    Args:
    input_text (str): The input text to be tokenized.

    Returns:
    list: A list of words.
    """
    assert isinstance(input_text, str), "Input should be a string"
    tokenized_words = input_text.split()
    return tokenized_words

def count_words(input_text):
    """
    Counts the occurrences of each word in the input text.

    Args:
    input_text (str): The input text to be counted.

    Returns:
    dict: A dictionary with words as keys and their counts as values.
    """
    assert isinstance(input_text, str), "Input should be a string"
    cleaned_text = clean_text(input_text)
    tokenized_words = tokenize(cleaned_text)
    word_count_dictionary = {}
    for word in tokenized_words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else:
            word_count_dictionary[word] = 1
    return word_count_dictionary

def count_lines(filename):
    """
    Counts the number of lines in a file.

    Args:
    filename (str): The path to the file.

    Returns:
    int: The number of lines in the file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return sum(1 for line in file)

def count_total_lines(filenames):
    """
    Counts the total number of lines in multiple files.

    Args:
    filenames (list): A list of file paths.

    Returns:
    int: The total number of lines across all files.
    """
    total_lines = 0
    for filename in filenames:
        total_lines += count_lines(filename)
    return total_lines

def count_total_words(filenames):
    """
    Counts the total number of words in multiple files.

    Args:
    filenames (list): A list of file paths.

    Returns:
    int: The total number of words across all files.
    """
    total_words = 0
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = tokenize(clean_text(content))
            total_words += len(words)
    return total_words

def count_raven_occurrences(filename):
    """
    Counts occurrences of the word 'raven' (case insensitive) in a file.

    Args:
    filename (str): The path to the file.

    Returns:
    dict: A dictionary with counts of 'raven' in lower and upper case.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        lc_count = content.lower().count('raven')
        uc_count = content.count('Raven')
        return {'lowercase': lc_count, 'uppercase': uc_count, 'total': lc_count + uc_count}
