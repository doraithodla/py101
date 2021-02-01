def word_freq1(str):
    """
    takes a string and calculates the word frequency table
    :param str: string input
    :return: frequency dictionary
    """
    frequency = {}
    for word in str.split():
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency


print(word_freq1("This is a test about test for this"))
