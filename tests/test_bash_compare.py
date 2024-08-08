import os, sys, subprocess, platform
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')));

import pytest
from tokenize_text import tokenize, clean_text
from tests.expected_failure_decorator import expected_to_fail


def test_clean_text_bash_comparison():
    # Test string
    test_string = "Hello, World! This is a Test."
    
    # Use clean_text function
    python_result = clean_text(test_string)
    
    # Use bash command to clean text
    bash_command = f"echo '{test_string}' | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]'"
    bash_result = subprocess.run(bash_command, shell=True, capture_output=True, text=True).stdout.strip()
    
    # Compare results
    assert python_result == bash_result, f"Python result: '{python_result}' does not match Bash result: '{bash_result}'"
