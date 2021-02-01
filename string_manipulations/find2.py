def substring_index(s, sub):
    """
    function to tell is substring in string and if yes then return the starting index
    :param s: full string
    :param sub: substring to be checked
    :return: -1 if not there else starting index of the substring
    """
    index = s.find(sub)
    return index


s = input("Enter the string: ")
sub = input("Enter the substring to find: ")
result = substring_index(s, sub)
if result == -1:
    print("Substring not found")
else:
    print("substring found at index", result)
