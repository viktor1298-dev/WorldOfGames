SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = "404"


def screen_cleaner():
    import os
    os.system('cls||clear')


def number_validation(number_list):
    if len(number_list) == 3:
        pre_number = 0
        while not number_list[1] <= pre_number <= number_list[2]:
            try:
                pre_number = int(input(number_list[0]))
                if not number_list[1] <= pre_number <= number_list[2]:
                    print("You did not enter a number from " + str(number_list[1]) + " to " + str(number_list[2]) + ".")
            except ValueError:
                print("You didn't enter a valid number.")
                pre_number = 0
        return pre_number

    elif len(number_list) == 1:
        pre_number = "0"
        while type(pre_number) is not float:
            try:
                pre_number = float(input(number_list[0]))
            except ValueError:
                print("You didn't enter a valid number.")
        return pre_number
