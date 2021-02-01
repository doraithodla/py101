# Noise words, also called stop words, are commonly used English words like any, of, and all.
def get_noise_words():
    s = input("Enter noise words seperated by a comma: ")
    # his,and,or,of,if,hi,hello,for,the
    return s.split(",")


print(get_noise_words())
