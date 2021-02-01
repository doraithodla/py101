noise_words = {"if", "and", "or", "the", "add", "a","is","to","of"}


def wordset(string):
    """
    converts a list of words to a set
    :param list: string input from the user
    :return: set object
    """
    string_set = set(string.split())
    return string_set


def clean_words(word_set):
    """
    function to remove all words in noise words
    :param word_set: set of words
    :return: list of clean words
    """
    return word_set.difference(noise_words)


words_set = wordset("a is a test to check the test of sets ")
print(clean_words(words_set))
