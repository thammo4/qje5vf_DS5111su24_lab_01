"""
This module contains tests for the base functionality of the project.

It includes imports and setup required for testing, such as adjusting the
Python path to include the project's root directory and importing custom
decorators like `expected_to_fail` from the `expected_failure_decorator` module.

Additionally, this module defines a constant `FRENCH_TEXT`, which is a
sample text in French that may be used in various test cases to ensure
proper handling of non-English text within the project.
"""

# pylint: disable=no-member
import os
import sys
import pytest
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from tests.expected_failure_decorator import expected_to_fail

FRENCH_TEXT = "_Mais le Corbeau, perché solitairement sur ce buste placide, parla ce seul mot comme si, son âme, en ce seul mot, il la répandait. Je ne proférai donc rien de plus: il n'agita donc pas de plume--jusqu'à ce que je fis à peine davantage que marmotter «D'autres amis déjà ont pris leur vol--demain il me laissera comme mes Espérances déjà ont pris leur vol.» Alors l'oiseau dit: «Jamais plus.»_"
