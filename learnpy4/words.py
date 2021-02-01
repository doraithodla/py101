class Words:
    def __init__(self, all_text):
        self.all_text = all_text

    def get_text(self):
        return self.all_text

    def get_words_list(self):
        return self.all_text.split()

    def get_word_count(self):
        return len(self.all_text.split())

    def get_line_count(self):
        return len(self.all_text.split("\n"))


text = """this is a test
to check the class a
now lets test it again"""
words = Words(text)
print(words.get_line_count())
print(words.get_word_count())
print(words.get_words_list())
