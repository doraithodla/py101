noise_words = {"if", "and", "or", "the", "add"}


def wordset(string):
    """
    converts a list of words to a set
    :param list: string input from the user
    :return: set object
    """
    string_set = set(string.split())

    print(string_set)
    print(noise_words)


wordset("a is a test to check the test of sets ")
