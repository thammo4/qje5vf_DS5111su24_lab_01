[![Python package](https://github.com/thammo4/qje5vf_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg)](https://github.com/thammo4/qje5vf_DS5111su24_lab_01/actions/workflows/validations.yml)

[![Python package](https://github.com/thammo4/qje5vf_DS5111su24_lab_01/actions/workflows/validations.yml/badge.svg)](https://github.com/thammo4/qje5vf_DS5111su24_lab_01/actions/workflows/validations.yml)
## Text Processing Functions

This project includes several text processing functions in `tokenize_text.py`:

- `clean_text(input_text)`: Converts text to lowercase and removes punctuation.
- `tokenize(input_text)`: Splits text into individual words.
- `count_words(input_text)`: Counts the occurrences of each word in the text.
- `count_lines(filename)`: Counts the number of lines in a file.
- `count_total_lines(filenames)`: Counts the total number of lines across multiple files.
- `count_total_words(filenames)`: Counts the total number of words across multiple files.
- `count_raven_occurrences(filename)`: Counts occurrences of the word 'raven' (case insensitive) in a file.

### Example Usage

Here's a simple example of how to use the `clean_text` and `count_words` functions:

```python
from tokenize_text import clean_text, count_words

text = "The Raven, by Edgar Allan Poe"
cleaned_text = clean_text(text)
word_counts = count_words(text)

print(f"Cleaned text: {cleaned_text}")
print(f"Word counts: {word_counts}")

# Output:
# Cleaned text: the raven by edgar allan poe
# Word counts: {'the': 1, 'raven': 1, 'by': 1, 'edgar': 1, 'allan': 1, 'poe': 1}


### Using `make all`

To automate the setup, text download, statistics generation, and testing processes, you can use the `make all` command. This command will:

1. Set up the Python virtual environment and install the required dependencies.
2. Download the specified text files from Project Gutenberg.
3. Generate statistics about the downloaded texts, including line and word counts for "The Raven" and total counts across all downloaded texts.
4. Run the test suite to ensure all functionalities are working correctly.

To use `make all`, simply run the following command in your terminal:

```bash
make all

