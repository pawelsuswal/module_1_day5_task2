"""Lotto game, guess 6 numbers from 1-49 range

    Usage:
    python app.py
    import app
    app.main
"""
from random import choices


def ask_user_for_input(text_for_user):
    """
    Take user input
    :param text_for_user: Message for user
    :type text_for_user: str
    :return: User input
    :rtype: str
    """

    return input(text_for_user)


def get_n_numbers_from_user(user_numbers_amount, min_digit, max_digit):
    """
    Ask user to provide n numbers form given range
    :param user_numbers_amount: AMount of numbers to provide by user
    :type user_numbers_amount: int
    :param min_digit: Minimal value for range from which user should pick number
    :type min_digit: int
    :param max_digit: Maximum value for range from which user should pick number
    :type max_digit: int
    :return: User input as int, wrong user input handled
    :rtype: int
    """
    user_numbers = []

    # asking user to provide requested amount of numbers
    for idx in range(user_numbers_amount):

        while len(user_numbers) < user_numbers_amount:
            if len(user_numbers) == 0:
                print("\nYou have not provided any number")
            else:
                print(f"\nYou have already provided those numbers: {user_numbers}")

            user_input = ask_user_for_input(f"Provide number from range {min_digit}-{max_digit}: ")

            # check is provided text is a number
            try:
                user_input = int(user_input)
                user_input_is_digit = True
            except ValueError:
                user_input_is_digit = False

            if not user_input_is_digit:
                print("\nInput data error!")
                print("It's not a number!")
                print("Your input must be numeric. Please try again.\n")
            elif user_input < min_digit or user_input > max_digit:
                print("\nInput data error!")
                print("Your number is not in range!\n")
            elif user_input in user_numbers:
                print("\nInput data error!")
                print("Your already provided this number!")
                print("Please provide unique numbers.\n")
            else:
                user_numbers.append(user_input)

    return user_numbers


def pick_n_random_number_from_given_range(user_numbers_amount, min_digit, max_digit):
    """
    Pick random n numbers from given range
    :param user_numbers_amount: Amount of numbers to be drawn
    :type user_numbers_amount: int
    :param min_digit: Minimal value for range from which number will be drawn
    :type min_digit: int
    :param max_digit: Maximum value for range from which number will be drawn
    :type max_digit: int
    :return: collection of drawn numbers
    :rtype: list
    """
    return choices(range(min_digit, max_digit + min_digit), k=user_numbers_amount)


def play_lotto_game():
    """
    Lotto game, ask user for 6 numbers from range 1-49, drawn 6 numbers from same range and check how many
    number of hits user have, user wins if hits are greater than 2
    :return: None
    """
    number_to_drawn = 6
    min_digit = 1
    max_digit = 49

    user_numbers = get_n_numbers_from_user(number_to_drawn, min_digit, max_digit)
    drawn_numbers = pick_n_random_number_from_given_range(number_to_drawn, min_digit, max_digit)

    # check how many hits user have
    # take number from user_numbers and iterate drawn_numbers looking for it, count every hit
    number_of_hits = sum(number in user_numbers for number in drawn_numbers)

    print(f'Your numbers are: {user_numbers}')
    print(f'Drawn numbers are: {drawn_numbers}\n')

    print(f"You have {number_of_hits} hits.")
    if number_of_hits >= 3:
        print("You win!")
    else:
        print("You loose!")


def main():
    if __name__ == "__main__":
        play_lotto_game()
