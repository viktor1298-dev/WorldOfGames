import random


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty + 1)
    return secret_number


def get_guess_from_user(difficulty):
    guessed_number = int(input("Please guess the random number from 1 to " + str(difficulty + 1) + ': '))
    if guessed_number < 1 or guessed_number > (difficulty + 1):
        print("You can only choose between 1 and ", difficulty)
        get_guess_from_user(difficulty)
    else:
        return guessed_number


def compare_results(secret_number, guessed_number):
    answer = 1
    while answer == 1:
        if secret_number == guessed_number:
            print("WOW YOU GOOD")
            answer = 0
        else:
            guessed_number = int(input("Bad choice, Please try again: "))


def play(difficulty):
    secret_number = generate_number(difficulty)
    guessed_number = get_guess_from_user(difficulty)
    return compare_results(secret_number, guessed_number)
