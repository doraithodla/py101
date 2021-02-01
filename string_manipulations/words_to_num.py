def words_to_num(words):
    """
    function to convert words to  a 2 digit number
    :param words: eg. twenty five
    :return: integer
    """
    words = words.lower()
    tens = ["", "ten", "twenty", "thrity", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', "ten", "eleven",
               "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    if words in tens:
        return tens.index(words) * 10
    elif words in numbers:
        return numbers.index(words)
    elif len(words.split()) > 2:
        print("invalid input")
        return -1
    first = words.split()[0]
    second = words.split()[1]
    return tens.index(first) * 10 + numbers.index(second)


print(words_to_num("fifty five"))
