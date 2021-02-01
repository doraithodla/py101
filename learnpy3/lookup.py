numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}


def lookup(n):
    """
    function to lookup a number in a dictionary and return the value
    :param number: integer
    :return: value from the dictionary
    """
    if n in numbers:
        return numbers[n]
    else:
        return "Number not found"


print(lookup(2))
print(lookup(20))
