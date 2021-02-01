def word_freq(str):
    str = str.split()
    str2 = []

    for i in str:
        if i not in str2:
            str2.append(i)
    for i in range(0, len(str2)):
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))


print(word_freq('This is a test about test for this'))


def word_freq1(str):
    frequency = {}
    for word in str.split():
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency


print(word_freq1("This is a test about test for this"))
