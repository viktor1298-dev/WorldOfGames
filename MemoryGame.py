from random import randint
from time import sleep


def generate_sequence(difficulty):
    list_size = difficulty
    sequence_list = [] * list_size
    for number in range(list_size):
        sequence_list.append(randint(1, 101))
    return sequence_list


def get_list_from_user(difficulty):
    list_size = difficulty
    user_list = [] * list_size
    for number in range(list_size):
        user_list.append(int(input("\rPlease enter the number you remember in the same order: ")))
    return user_list


def is_list_equal(sequence_list, user_list):
    if sequence_list == user_list:
        print("Congratulations! You have guessed the correct order!")
        return True
    else:
        print("Wrong Order :( ")
        return False


def play(difficulty):
    generated_list = generate_sequence(difficulty)
    print(generated_list, end="")
    sleep(0.7)
    user_list = get_list_from_user(difficulty)
    result = is_list_equal(generated_list, user_list)
    return result
