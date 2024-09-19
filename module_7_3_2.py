import re


class WordsFinder:
    def __init__(self, *file_name):
        self.file_names = tuple(file_name)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                line = file.read().lower()
                new_line = re.sub(r'[^\w\s]', '', line)
                words = new_line.split()
            all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        find_word = {}
        for name, words in self.get_all_words().items():
            if word in words:
                find_word[name] = words.index(word) + 1
        return find_word

    def count(self, word):
        word = word.lower()
        find_word = {}
        for name, words in self.get_all_words().items():
            if word in words:
                find_word[name] = words.count(word)
        return find_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
