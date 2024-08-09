"""


The tests included in this module cover a variety of scenarios:
- Cleaning English and French text samples.
- Handling text with punctuation.
- Ensuring text files are cleaned properly.

and conditions, ensuring the function's robustness and correctness.
"""

import string
from qje5vf.tokenize_text import clean_text
from .test_base import *

def test_clean_text_french():
    """
    Test the clean_text function on a sample of French text.

    The function checks if the text is properly cleaned by removing punctuation,
    converting to lowercase, and preserving special characters like accents.
    """
    expected_output = "mais le corbeau perché solitairement sur ce buste placide parla ce seul mot comme si son âme en ce seul mot il la répandait je ne proférai donc rien de plus il nagita donc pas de plumejusquà ce que je fis à peine davantage que marmotter «dautres amis déjà ont pris leur voldemain il me laissera comme mes espérances déjà ont pris leur vol» alors loiseau dit «jamais plus»"
    cleaned_text = clean_text(FRENCH_TEXT)
    assert cleaned_text == expected_output, f"Failed to clean French text. Got: {cleaned_text}"


# List of files to test
FILES_TO_TEST = ["pg10031.txt", "pg1063.txt", "pg1064.txt", "pg10947.txt",
                 "pg17192.txt", "pg32037.txt", "pg50852.txt", "pg51060.txt", "pg932.txt"]

@pytest.mark.parametrize("filename", FILES_TO_TEST)
def test_clean_text_on_files(filename):
    """
    Test the clean_text function on multiple text files.

    This function checks if the text from each file is properly cleaned by:
    - Removing punctuation
    - Converting all text to lowercase
    - Ensuring the cleaned text is not empty
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_text = clean_text(content)

    assert cleaned_text.islower(
    ), f"Text in file {filename} is not all lowercase"
    assert all(char not in string.punctuation for char in cleaned_text), f"Punctuation found in cleaned text of {filename}"
    assert len(cleaned_text) > 0, f"Cleaned text from file {filename} is empty"


@pytest.mark.skip(reason="No non-Latin script text available for testing")
def test_clean_text_non_latin_script(non_latin_text="placeholder_for_non_latin_text"):
    """
    Test the clean_text function on a sample of non-Latin script text.

    The function checks if the text is properly cleaned by removing non-alphanumeric
    characters and ensuring that the text is in lowercase.
    """
    cleaned = clean_text(non_latin_text)
    assert len(cleaned) > 0, "Cleaned non-Latin text is empty"
    assert cleaned.islower(), "Cleaned non-Latin text contains uppercase characters"
    assert all(char.isalnum() or char.isspace()
               for char in cleaned), "Cleaned non-Latin text contains non-alphanumeric characters"


@pytest.mark.parametrize("filename", ['pg1064.txt', 'pg17192.txt', 'pg32037.txt', 'pg51060.txt'])
def test_clean_text_n_files(filename):
    """
    Test the clean_text function on a subset of text files.

    The function checks if the text is properly cleaned by:
    - Converting all text to lowercase
    - Removing commas and periods
    - Ensuring the cleaned text is not empty
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned = clean_text(content)
    assert cleaned.islower(), f"Clean text failed to convert {filename} to lowercase"
    assert ',' not in cleaned, f"Clean text failed: comma removal {filename}"
    assert '.' not in cleaned, f"Clean text failed: period removal {filename}"
    assert len(cleaned) > 0, f"Clean text empty: {filename}"


@pytest.mark.parametrize("input_text, expected_output", [
    ("It's a Raven!", "its a raven"),
    ("What's it doing here?", "whats it doing here"),
    ("(Nevermore)", "nevermore"),
])
def test_clean_text_punctuation(input_text, expected_output):
    """
    Test the clean_text function on strings with punctuation.

    This function checks if punctuation is correctly removed and if the resulting
    text matches the expected output.
    """
    cleaned = clean_text(input_text)
    assert cleaned == expected_output, f"Clean text failed on: {input_text}\nExpected: {expected_output}\nGot: {cleaned}"


def test_clean_text_basic():
    """
    Test the clean_text function on a basic sample of English text.

    This function checks if the text is properly cleaned by removing punctuation
    and converting to lowercase.
    """
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    expected = 'but the raven sitting lonely on the placid bust spoke only that one word as if his soul in that one word he did outpour'
    assert clean_text(
        text) == expected, f"Clean text failed on sample text: {text}"


def test_clean_text_uppercase():
    """
    Test the clean_text function on an uppercase text sample.

    This function checks if the text is correctly converted to lowercase.
    """
    text = 'THE RAVEN'
    expected = 'the raven'
    assert clean_text(
        text) == expected, f"Clean text failed on uppercase text: {text}"


def test_clean_text_file():
    """
    Test the clean_text function on the contents of a text file.

    This function checks if the text is properly cleaned by:
    - Removing commas
    - Converting to lowercase
    - Ensuring specific words are preserved (e.g., 'raven')
    """
    with open('pg17192.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned = clean_text(content)
    assert 'raven' in cleaned, "Clean text failed to preserve 'raven' in The Raven"
    assert ',' not in cleaned, "Clean text failed to remove commas in The Raven"
    assert cleaned.islower(), "Clean text failed to convert The Raven to lowercase"


def test_clean_text_french_file():
    """
    Test the clean_text function on the contents of a French text file.

    This function checks if the text is properly cleaned by:
    - Removing commas
    - Converting to lowercase
    - Preserving accented characters
    """
    with open('pg14082.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    cleaned = clean_text(content)
    assert 'é' in cleaned, "Clean text removed accented characters in French text"
    assert ',' not in cleaned, "Clean text failed to remove commas in French text"
    assert cleaned.islower(), "Clean text failed to convert French text to lowercase"


@expected_to_fail
def test_clean_text_fail():
    """
    Test case designed to fail for the clean_text function.

    This function checks if punctuation is unexpectedly removed when it should be retained.
    """
    text = 'But the Raven, sitting lonely on the placid bust, spoke only That one word, as if his soul in that one word he did outpour.'
    cleaned = clean_text(text)
    assert ',' in cleaned, "Clean text unexpectedly removed punctuation"
