"""
slkdfjalskdfjaskfuahweriqukhjwek
type two errorz
"""
from test_base import *
from tokenize_text import clean_text, tokenize

@pytest.mark.integration
def test_clean_and_tokenize_integration():
    """
    Integration test for cleaning and tokenizing a simple text string.

    Given:
        A text string "The Raven, by Edgar Allan Poe"
    When:
        The text is cleaned and tokenized using clean_text and tokenize functions.
    Then:
        The tokens should be ['the', 'raven', 'by', 'edgar', 'allan', 'poe'].
    """
    text = "The Raven, by Edgar Allan Poe"
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    assert tokens == ['the', 'raven', 'by', 'edgar', 'allan', 'poe']


@pytest.mark.integration
def test_multiple_sentences_integration():
    """
    Integration test for cleaning and tokenizing a multi-sentence text string.

    Given:
        A text string "Once upon a midnight dreary. While I pondered, weak and weary."
    When:
        The text is cleaned and tokenized using clean_text and tokenize functions.
    Then:
        - The number of tokens should be greater than 5.
        - The tokens list should include 'midnight', 'dreary', and 'pondered'.
    """
    text = "Once upon a midnight dreary. While I pondered, weak and weary."
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    assert len(tokens) > 5  # Ensure we have multiple tokens
    assert 'midnight' in tokens
    assert 'dreary' in tokens
    assert 'pondered' in tokens
