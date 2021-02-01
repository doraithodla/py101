def int2words(num):
    d = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty',
        30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
        70: 'seventy', 80: 'eighty', 90: 'ninety'
    }
    h = [100, 'hundred', 'hundred and']
    k = [h[0] * 10, 'thousand', 'thousand,']
    m = [k[0] * 1000, 'million', 'million,']
    b = [m[0] * 1000, 'billion', 'billion,']
    t = [b[0] * 1000, 'trillion', 'trillion,']
    if num < 20:
        return d[num]
    if num < 100:
        div_, mod_ = divmod(num, 10)
        return d[num] if mod_ == 0 else d[div_ * 10] + '-' + d[mod_]
    else:
        if num < k[0]:
            divisor, word1, word2 = h
        elif num < m[0]:
            divisor, word1, word2 = k
        elif num < b[0]:
            divisor, word1, word2 = m
        elif num < t[0]:
            divisor, word1, word2 = b
        else:
            divisor, word1, word2 = t
        div_, mod_ = divmod(num, divisor)
        if mod_ == 0:
            return '{} {}'.format(int2words(div_), word1)
        else:
            return '{} {} {}'.format(int2words(div_), word2, int2words(mod_))


n = int(input("Enter the number to print in words: "))
print(int2words(n))
