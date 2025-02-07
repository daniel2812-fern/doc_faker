from collections import Counter
import string

def count_common_words(str1, str2):
    # Function to remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Convert strings to lowercase and remove punctuation
    str1 = str1.lower().translate(translator)
    str2 = str2.lower().translate(translator)
    
    # Tokenize the strings into words
    words_str1 = str1.split()
    words_str2 = str2.split()
    
    # Create Counter objects
    counter1 = Counter(words_str1)
    counter2 = Counter(words_str2)
    
    # Find common words and count them
    common_words = counter1 & counter2
    return sum(common_words.values())

# Example usage
str1 = "Python is great; Python is versatile."
str2 = "Java is also popular! Python is great too."
common_word_count = count_common_words(str1, str2)
print(common_word_count)  # Output: 3 (is, python, great)
