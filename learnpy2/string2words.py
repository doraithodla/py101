def string_to_words(string):
    """
    function to split a string into words
    :param string: string entered by the user
    :return:list of words
    """
    words = []
    word = ""

    for character in string:
        if character == " ":
            words.append(word)
            word = ""
        else:
            word = word + character
    words.append(word)
    return words


s = input("Enter the string: ")

print(string_to_words(s))
print(s.split())
