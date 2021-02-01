# wordfreq2 - rewrite the wordfreq program to take the text from a file and count the words

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


def read(file_name):
    """
    reads a file and returns the number of lines in the file
    :param file_name: name of the file to be read
    :return: number of lines in the file
    """
    with open(file_name, "r") as f:
        text = f.read()
        return text


file_text = read("something.txt")
print(word_freq1(file_text))
