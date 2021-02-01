def get_number(index):
    """
    function to look up numbers and convert them to strings
    :param index: one digit number
    :return: number in string
    """
    number = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    return number[index]


n = int(input("Enter a single digit number: "))
print(get_number(n))
