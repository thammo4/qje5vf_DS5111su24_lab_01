# FILE: tests/test_clean_text.py
import sys
import os
import string
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tokenize_text import clean_text
from tests.expected_failure_decorator import expected_to_fail


french_text = "_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"



def test_clean_text_french():
    expected_output = (
        "mais le corbeau perché solitairement sur ce buste placide parla "
        "ce seul mot comme si son âme en ce seul mot il la répandait je ne "
        "proférai donc rien de plus il nagita donc pas de plumejusquà ce "
        "que je fis à peine davantage que marmotter dautres amis déjà ont "
        "pris leur voldemain il me laissera comme mes espérances déjà ont "
        "pris leur vol alors loiseau dit jamais plus"
    )
    cleaned_text = clean_text(french_text)
    assert cleaned_text == expected_output, f"Failed to clean French text. Got: {cleaned_text}"






# List of files to test
files_to_test = ["pg10031.txt", "pg1063.txt", "pg1064.txt", "pg10947.txt", "pg17192.txt", "pg32037.txt", "pg50852.txt", "pg51060.txt", "pg932.txt"]

@pytest.mark.parametrize("filename", files_to_test)
def test_clean_text_on_files(filename):
    with open(filename, 'r') as file:
        content = file.read()
    
    # Clean the text using the provided function
    cleaned_text = clean_text(content)
    
    # Assert that the cleaned text is in lowercase
    assert cleaned_text.islower(), f"Text in file {filename} is not all lowercase"
    
    # Assert that punctuation is removed
    punctuation_marks = string.punctuation
    assert all(char not in punctuation_marks for char in cleaned_text), f"Punctuation found in cleaned text of {filename}"
    
    # Assert that the cleaned text is not empty
    assert len(cleaned_text) > 0, f"Cleaned text from file {filename} is empty"







@pytest.mark.skip(reason="No non-Latin script text available for testing")
def test_clean_text_non_latin_script(non_latin_text="placeholder_for_non_latin_text"):
    # This test is a placeholder for future testing of clean_text() with non-Latin scripts
    # It is skipped because we currently don't have appropriate test data
    cleaned = clean_text(non_latin_text)
    assert len(cleaned) > 0, "Cleaned non-Latin text is empty"
    assert cleaned.islower(), "Cleaned non-Latin text contains uppercase characters"
    assert all(char.isalnum() or char.isspace() for char in cleaned), "Cleaned non-Latin text contains non-alphanumeric characters"





@pytest.mark.parametrize("filename", ['pg1064.txt', 'pg17192.txt', 'pg32037.txt', 'pg51060.txt'])
def test_clean_text_n_files(filename):
    with open(filename, 'r') as f:
        content = f.read()
    cleaned = clean_text(content);
    assert cleaned.islower(), f"Clean text failed to convert {filename} to LC";
    assert ',' not in cleaned, f"Clean text failed: comma removal {filename}";
    assert '.' not in cleaned, f"Clean text failed: period removal {filename}"
    assert len(cleaned) > 0, f"Clean text empty: {filename}"



@pytest.mark.parametrize("input_text, expected_output", [
    ("It's a Raven!", "its a raven"),
    ("What's it doing here?", "whats it doing here"),
    ("(Nevermore)", "nevermore"),
    ("The Raven - by Edgar Allan Poe", "the raven by edgar allan poe"),
    ("'Quoth the Raven, \"Nevermore.\"'", "quoth the raven nevermore"),
    ("!!!Exciting!!! ???Question??? ***Important***", "exciting question important"),
    ("Email: raven@example.com; Phone: 123-456-7890", "email ravenexamplecom phone 1234567890"),
    ("$100.00 + 20% = $120.00", "10000 20 12000"),
    ("The end.\nNew line.", "the end new line"),
])
def test_clean_text_punctuation(input_text, expected_output):
    # Given a string with various punctuation marks and special characters
    # When I pass the string to the clean_text() function
    # Then I should get a string with all punctuation removed
    cleaned = clean_text(input_text)
    assert cleaned == expected_output, f"Clean text failed on: {input_text}\nExpected: {expected_output}\nGot: {cleaned}"

def test_clean_text_basic():
    # Given a string with mixed case and punctuation
    # When I pass the string to the clean_text() function
    # Then I should get a lowercase string with punctuation removed
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected = 'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour'
    assert clean_text(text) == expected, f"Clean text failed on sample text: {text}"

def test_clean_text_uppercase():
    # Given an uppercase string
    # When I pass the string to the clean_text() function
    # Then I should get a lowercase string
    text = 'THE RAVEN'
    expected = 'the raven'
    assert clean_text(text) == expected, f"Clean text failed on uppercase text: {text}"

def test_clean_text_punctuation():
    # Given a string with various punctuation marks
    # When I pass the string to the clean_text() function
    # Then I should get a string with all punctuation removed
    text = "It's a Raven! What's it doing here? (Nevermore)"
    expected = "its a raven whats it doing here nevermore"
    assert clean_text(text) == expected, f"Clean text failed on punctuated text: {text}"

def test_clean_text_file():
    # Given the content of "The Raven" file
    # When I pass the content to the clean_text() function
    # Then I should get a cleaned version of the text
    with open('pg17192.txt', 'r') as file:
        content = file.read()
    cleaned = clean_text(content)
    assert 'raven' in cleaned, "Clean text failed to preserve 'raven' in The Raven"
    assert ',' not in cleaned, "Clean text failed to remove commas in The Raven"
    assert cleaned.islower(), "Clean text failed to convert The Raven to lowercase"

def test_clean_text_french():
    # Given a French text with accented characters
    # When I pass the content to the clean_text() function
    # Then I should get a cleaned version of the text with accents preserved
    with open('pg14082.txt', 'r') as file:
        content = file.read()
    cleaned = clean_text(content)
    assert 'é' in cleaned, "Clean text removed accented characters in French text"
    assert ',' not in cleaned, "Clean text failed to remove commas in French text"
    assert cleaned.islower(), "Clean text failed to convert French text to lowercase"

@expected_to_fail
def test_clean_text_fail():
    # Given a string with punctuation
    # When I pass the string to the clean_text() function
    # Then I expect it to keep the punctuation (which it shouldn't)
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    cleaned = clean_text(text)
    assert ',' in cleaned, "Clean text unexpectedly removed punctuation"
