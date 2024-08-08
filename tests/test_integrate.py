# FILE: tests/test_integrate.py
import sys
import os
import string
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tokenize_text import clean_text, tokenize



@pytest.mark.integration
def test_clean_and_tokenize_integration():
    text = "The Raven, by Edgar Allan Poe"
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    assert tokens == ['the', 'raven', 'by', 'edgar', 'allan', 'poe']


@pytest.mark.integration
def test_multiple_sentences_integration():
    text = "Once upon a midnight dreary. While I pondered, weak and weary."
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    assert len(tokens) > 5  # Ensure we have multiple tokens
    assert 'midnight' in tokens
    assert 'dreary' in tokens
    assert 'pondered' in tokens
