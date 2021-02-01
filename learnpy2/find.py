def contains_substring(s, sub):
    """
    function to tell if substring is in the string or not
    :param s: full string
    :param sub: sub string to be checked
    :return: True or False
    """
    if sub in s:
        return True
    else:
        return False


s = input("Enter the string: ")
sub = input("Enter the substring to find: ")
print(contains_substring(s, sub))
