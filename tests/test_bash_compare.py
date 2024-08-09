"""
This module contains a test that compares the output of the clean_text function from
the tokenize_text module with the equivalent text processing done using a Bash command.

The test ensures that the Python implementation for cleaning text (i.e., converting text
to lowercase and removing punctuation) produces the same result as a corresponding Bash
command pipeline.
"""

import subprocess
import platform
from qje5vf.tokenize_text import tokenize, clean_text
from .test_base import *

def test_clean_text_bash_comparison():
    """
    doc my string
    """

    # Test string
    test_string = "Hello, World! This is a Test."

    # Use clean_text function
    python_result = clean_text(test_string)

    # Use bash command to clean text
    bash_command = f"echo '{test_string}' | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'"
    bash_result = subprocess.run(bash_command, shell=True, capture_output=True, text=True
                                 ).stdout.strip()

    # Compare results
    assert python_result == bash_result, f"Python result: {python_result} does not match Bash result: {bash_result}"
