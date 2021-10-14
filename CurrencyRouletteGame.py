import random
import requests


def get_money_interval(difficulty, random_number):
    response = requests.get('https://api.currencyfreaks.com/latest?apikey=68c8eb96b1f943f28b06b2aa428f00d9')
    ils_rate = float(response.json()['rates']['ILS'])
    total = random_number * ils_rate
    money_interval = [total - (5 - difficulty), total + (5 - difficulty)]
    return money_interval


def get_guess_from_user(random_number):
    answer = False
    while not answer:
        try:
            user_guess = float(input("Please try to estimate the current value of {} USD in ILS: ".format(random_number)))
            if user_guess > 0:
                answer = True
                return user_guess
            else:
                print('That is not a number greater than 0, try again please')
        except ValueError:
            print('That is not a number, try again please')


def play(difficulty):
    random_number = float(random.randint(1, 100))
    money_interval = get_money_interval(difficulty, random_number)
    user_guess = get_guess_from_user(random_number)
    answer = 1
    while answer == 1:
        if money_interval[0] <= float(user_guess) <= money_interval[1]:
            print("Good Guess !")
            answer = 0
            return True
        else:
            print("Bad Guess ! Please try again :) ")
            user_guess = get_guess_from_user(random_number)
