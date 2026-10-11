
class Agent:
    def __init__(self, words, target_length):
        self.words_set = set(words)
        self.initialize(target_length)

    def initialize(self, target_length):
        self.target_length = target_length
        self.local_words_set = {word for word in self.words_set if len(word) == self.target_length}