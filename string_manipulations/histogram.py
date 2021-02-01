s = input("Enter the string to remove duplicated from: ")


def remove_dup(list):
    list2 = []
    for elem in list:
        if elem not in list2:
            list2.append(elem)
    return list2


print(remove_dup(s.split()))

print(set(s.split()))
