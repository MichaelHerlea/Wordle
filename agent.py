from wordle import GuessResult

class Agent:
    def __init__(self, words, target_length):
        self.words_set = words
        self.initialize(target_length)

    def initialize(self, target_length):
        self.target_length = target_length
        self.local_words_set = {word for word in self.words_set if len(word) == self.target_length}
        self.green_characters = {}
        self.yellow_characters = {}
        self.excluded_characters = set()

    def process_feedback(self, feedback: GuessResult):
        if not feedback.is_valid:
            return
        for i in range(self.target_length):
            letter = feedback.guess[i]
            color = feedback.feedback[i]

            if color == "G":
                if letter not in self.green_characters: self.green_characters[letter] = set()
                self.green_characters[letter].add(i)
            elif color == "Y":
                if letter not in self.yellow_characters: self.yellow_characters[letter] = set()
                self.yellow_characters[letter].add(i)
            elif color == "B":
                self.excluded_characters.add(letter)

        self.local_words_set = {word for word in self.local_words_set if self.matches_feedback_constraints(word)}

    def matches_feedback_constraints(self, word):
        word_set = set(word)
        for character in self.excluded_characters:
            if character in word_set:
                return False
        for character, positions in self.green_characters.items():
            for index in positions:
                if word[index] != character:
                    return False
        for character, positions in self.yellow_characters.items():
            if character not in word_set:
                return False
            for index in positions:
                if word[index] == character:
                    return False
        return True

    def make_guess(self):
        max_value = (-1, "")
        for word in self.local_words_set:
            local_max_value = self.target_length
            for character in word:
                if character in self.green_characters:
                    local_max_value -= 1
                elif character in self.yellow_characters:
                    local_max_value -= 0.5
            if local_max_value == self.target_length: return word
            if local_max_value > max_value[0]:
                max_value = (local_max_value, word)
        return max_value[1]
