import random as rd

CHECKED_DIGIT = '-'
NEAR = '+'
NOT_EXIST = '_'
EXACT_DIGIT = "*"


instructions = "Welcome to the mastermind game\n" \
               "In this game the computer becomes the code-maker and you are the code-breaker!\n" \
               "1. The code-breaker chooses the length of the code\n" \
               "2. The code-maker chooses a pattern of numbers in the chosen length\n" \
               "3. You need to guess the number\n" \
               "4. If you select a number that exists in the code, in the right place," \
               " you'll see the * sign\n" \
               "5. If you select a number that exists in the code, but not in the right place," \
               " you'll see the + sign\n" \
               "6. If you select a number that doesn't exists in the code, you'll see the _ sign\n" \
               "7. The game will continue until you will guess the number that code-maker chose\n" \
               "Let's get started!\n"


def mind_master():
    length_of_number = None
    code_to_crack = []
    all_guesses = []

    easy_level_game_status = []
    hard_level_game_status = []

    def game_instructions():
        print(instructions)

    def generate_number():
        while True:
            nonlocal length_of_number
            length_of_number = int(input("Choose the length of the code to break: "))
            if length_of_number > 10:
                print("You can select up to 10 digits")
            elif length_of_number < 1:
                print("You must select at least one digit")
            else:
                break

        nonlocal code_to_crack
        code_to_crack = rd.sample(range(1, 10), length_of_number)
        print("Code: " + str(code_to_crack))

    def time_to_guess():
        while True:
            users_guess = input("Guess the number in the length of {0}: ".format(length_of_number))
            if len(users_guess) != length_of_number:
                print("Your guess must be a number in the length of {0}".format(length_of_number))
            else:
                break
        return users_guess

    def check_if_game_over(p_users_guess):
        counter = 0
        for x, y in zip(p_users_guess, code_to_crack):
            if x == y:
                counter += 1
            if counter == length_of_number:
                return True

    def evaluate_guess(p_users_guess):
        el_new_state = []
        hl_new_state = []
        copy_of_original_code = list(code_to_crack)
        copy_of_original_guess = list(p_users_guess)
        
        for pos, digit in enumerate(copy_of_original_guess):
            if digit == copy_of_original_code[pos]:
                el_new_state.append(str(digit))
                hl_new_state.append(EXACT_DIGIT)
                copy_of_original_code[pos] = CHECKED_DIGIT
                copy_of_original_guess[pos] = CHECKED_DIGIT
            else:
                el_new_state.append(NOT_EXIST)

        for pos, digit in enumerate(copy_of_original_guess):
            if copy_of_original_guess[pos] == CHECKED_DIGIT:
                continue
            if digit in copy_of_original_code:
                loc = copy_of_original_code.index(digit)
                el_new_state[pos] = NEAR
                hl_new_state.append(NEAR)
                copy_of_original_code[loc] = CHECKED_DIGIT
                copy_of_original_guess[pos] = CHECKED_DIGIT

        easy_level_game_status.append(''.join([char for char in el_new_state]))
        hard_level_game_status.append(''.join([char for char in hl_new_state]))
        print(easy_level_game_status)

    def print_game_status():
        print()
        for users_guess, el_state, hl_state in zip(all_guesses, easy_level_game_status, hard_level_game_status):
            print("Your guess:\t\tEasy Level:\t\tHard Level:")
            print(f"{users_guess}\t\t{el_state}\t\t{hl_state}")

    game_instructions()
    generate_number()

    the_answer_is_correct = False
    while not the_answer_is_correct:
        get_the_guess = time_to_guess()

        all_guesses.append(get_the_guess)
        guess_as_list = []
        for elem in get_the_guess:
            guess_as_list.append(int(elem))

        if not check_if_game_over(guess_as_list):
            evaluate_guess(guess_as_list)
            print_game_status()
        else:
            print(f"You guessed it right!\nThe code was {''.join([str(item) for item in code_to_crack])}! "
                  f"Congratulations!")

            the_answer_is_correct = True


if __name__ == '__main__':
    while True:
        mind_master()
        play_again = input("Play again? (y/n)\n")
        if play_again != 'y':
            print("OK, maybe next time!")
            break
