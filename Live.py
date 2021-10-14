from GuessGame import play as guess_game_play
from MemoryGame import play as memory_game_play
from CurrencyRouletteGame import play as currency_game_play
from Score import add_score
from Utils import number_validation


def welcome():
    print("Hello " + input("Please enter your name here: ") + " and welcome to the World of Games!" +
          "\n" + "Here you can find many cool games to play." + "\n")


def load_game():
    print("""Please Choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
        2. Guess Game - guess a number and see if you chose like the computer did
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    game_type = number_validation(["Which game do you want to play? Choose from 1 to 3: ", 1, 3])
    difficulty = number_validation(["Please Choose the game difficulty from 1 to 5: ", 1, 5])
    if game_type == 1:
        memory_game_play(difficulty)
        add_score(difficulty)
    elif game_type == 2:
        guess_game_play(difficulty)
        add_score(difficulty)
    elif game_type == 3:
        currency_game_play(difficulty)
        add_score(difficulty)
    return difficulty, game_type
