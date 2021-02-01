def convert(value1):
    """
    converts a list to dictionary and vice versa
    param value1: can be a dict or a  list
    return: a dict or a list
    """
    if type(value1) == dict:
        listt = []
        for key, value in value1.items():
            temp = [key, value]
            listt.extend(temp)
        return listt
    if type(value1) == list:
        Dict = {}
        i = 0
        for item in value1:
            Dict[value1[i][0]] = value1[i][1:]
            i = i + 1
        return Dict


dict1 = {'a': [1, 2], 'b': [3], 'c': [4, 5]}
lst1 = [['a', 1, 2], ['c', 4, 5], ['b', 3]]

print(convert(dict1))
print(convert(lst1))

#
# def convertDL(val):
#     if isinstance(val, dict):
#         return [[k] + v for k, v in val.iteritems()]
#     return {v[0]: v[1:] for v in val}
