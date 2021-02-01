def remove_duplicates(string):
    """
    function to remove duplicate words from a string
    :param string: string input by the user
    :return: string with duplicates removed
    """
    uniqs = ""
    for x in string.split():
        if not (x in uniqs):
            uniqs = uniqs + x + " "
    return uniqs


print(remove_duplicates("this is a test to test the function to remove the duplicates"))
