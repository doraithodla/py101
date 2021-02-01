# wordcount - open a file read the entire text, split it and count the words and print it
def word_count(words):
    """
    takes a list of words and returns the length of the list
    :param words: list of words
    :return: integer length
    """
    return len(words)


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
print(word_count(file_text.split()))
