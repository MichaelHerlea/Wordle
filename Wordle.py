import random

class WordleGame:
    def __init__(self, words, number_of_guesses=5):
        self.words_set = words
        self.words_list = list(self.words_set)
        self.initialize(number_of_guesses)

    def initialize(self, number_of_guesses=5):
        self.target_word = random.choice(self.words_list)
        self.target_word_length = len(self.target_word)
        self.target_word_set = set(self.target_word)
        self.number_of_guesses = number_of_guesses

    def make_guess(self, guess):
        output = GuessResult(guess)
        if len(guess) != self.target_word_length:
            output.feedback = "Invalid guess length."
            output.is_valid = False
            return output
        if guess not in self.words_set:
            output.feedback = "Invalid word."
            output.is_valid = False
            return output
        if self.number_of_guesses <= 0:
            output.feedback = "No guesses left."
            output.is_valid = False
            output.is_game_over = True
            return output
        self.number_of_guesses -= 1

        feedback = []
        for i in range(self.target_word_length):
            if guess[i] == self.target_word[i]:
                feedback.append("G")  # Green
            elif guess[i] in self.target_word_set:
                feedback.append("Y")  # Yellow
            else:
                feedback.append("B")  # Black
        output.feedback = ''.join(feedback)

        if output.feedback == "G" * self.target_word_length:
            output.is_won = True
            output.is_game_over = True

        if self.number_of_guesses <= 0:
            output.is_game_over = True
        return output

class GuessResult:
    def __init__(self, guess, feedback=None, is_valid_guess=True, is_won=False, is_game_over=False):
        self.guess = guess
        self.feedback = feedback
        self.is_valid = is_valid_guess
        self.is_won = is_won
        self.is_game_over = is_game_over

    def to_string(self): # for debugging purposes
        return f"Guess: {self.guess}, Feedback: {self.feedback}, Valid: {self.is_valid}, Won: {self.is_won}, Game Over: {self.is_game_over}"