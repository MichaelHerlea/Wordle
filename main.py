from wordle import WordleGame
from agent import Agent
import json

#words = set(json.load(open("words_dictionary.json")))
words = set(json.load(open("words.json")))
tile_backgrounds = {"G": "\033[42m", "Y": "\033[43m", "B": "\033[100m"}

wordle_game = WordleGame(words, 100)
agent = Agent(words, wordle_game.target_word_length)

while True:
    #guess = input(f"Enter a {wordle_game.target_word_length}-letter word: ").strip().lower()
    guess = agent.make_guess()
    guess_result = wordle_game.make_guess(guess)
    agent.process_feedback(guess_result)
    if guess_result.is_valid:
        tiles = "".join(
            f"{tile_backgrounds[color]} {letter.upper()} \033[0m"
            for letter, color in zip(guess, guess_result.feedback)
        )
        print(tiles)
    else:
        print(guess_result.feedback)

    if guess_result.is_game_over:
        if guess_result.is_won:
            print("Congratulations! You won!")
        else:
            print(f"Game over! The word was: {wordle_game.target_word}")
        break
        wordle_game.initialize()
        agent.initialize(wordle_game.target_word_length)