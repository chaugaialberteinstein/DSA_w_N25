# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.
#
# Example:
#
# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
# count_word_frequency(words)
# Output:
#
#  {'apple': 3, 'orange': 2, 'banana': 1}


def count_word_frequency(words):
    new_dict = {}
    for i in words:
        if i in new_dict:
            new_dict[i] += 1
        else:
            new_dict[i] = 1
    return new_dict

