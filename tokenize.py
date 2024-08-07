import string

def clean_text(input_text):
    """
    Cleans the input text by converting it to lowercase and removing punctuation.
    
    Args:
    input_text (str): The input text to be cleaned.
    
    Returns:
    str: The cleaned text.
    """
    # Check input type
    assert isinstance(input_text, str), "Input should be a string"
    
    # Convert to lowercase
    cleaned_text = input_text.lower()
    
    # Remove punctuation
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
    # Check input type
    assert isinstance(input_text, str), "Input should be a string"
    
    # Split the text into words
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
    # Check input type
    assert isinstance(input_text, str), "Input should be a string"
    
    # Clean and tokenize the text
    cleaned_text = clean_text(input_text)
    tokenized_words = tokenize(cleaned_text)
    
    # Count the occurrences of each word
    word_count_dictionary = {}
    for word in tokenized_words:
        if word in word_count_dictionary:
            word_count_dictionary[word] += 1
        else:
            word_count_dictionary[word] = 1
    
    return word_count_dictionary

# Example usage
if __name__ == "__main__":
    sample_text = "The quick brown fox jumps over the lazy dog";

    cleaned_text = clean_text(sample_text)
    assert isinstance(cleaned_text, str), "Return type should be a string"
    print("Cleaned text:", cleaned_text)
    
    tokenized_words = tokenize(cleaned_text)
    assert isinstance(tokenized_words, list), "Return type should be a list"
    print("Tokens:", tokenized_words)
    
    word_count_dictionary = count_words(sample_text)
    assert isinstance(word_count_dictionary, dict), "Return type should be a dictionary"
    print("Word counts:", word_count_dictionary)
