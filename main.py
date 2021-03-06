import math
import random


def print_hi():
    print("Hi there!")
    print('-' * 45)
    print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
    print('-' * 45)


def initial(num):
    num[0] = random.randint(1, 9)
    while len(num) != len(set(num)):
        for i in range(1, 4):
            num[i] = random.randint(0, 9)


def check_input(number_of_attempts, guess_str):
    if not guess_str.isdecimal():
        print("This is not a number. Try again.")
        number_of_attempts += 1
        return take_input(number_of_attempts)
    elif len(guess_str) != 4:
        print("This is not a valid length. Try again.")
        number_of_attempts += 1
        return take_input(number_of_attempts)
    elif len(guess_str) != len(set(guess_str)):
        print("This input contains duplicate numbers. Try again.")
        number_of_attempts += 1
        return take_input(number_of_attempts)
    elif guess_str[0] == '0':
        print("This input starts with 0. Try again.")
        number_of_attempts += 1
        return take_input(number_of_attempts)
    else:
        lst = split_guess(guess_str)
        guess = lst[:]
        return guess


def take_input(number_of_attempts):
    guess_str = input("Take your guess #" + str(number_of_attempts) + ":\n")
    print('-' * 45)
    guess = check_input(number_of_attempts, guess_str)
    return guess

def split_guess(guessed):
    guessed_int = int(guessed)
    guessed_list = [0, 0, 0, 0]
    for i in range(4):
        guessed_list[3 - i] = guessed_int % 10
        guessed_int -= guessed_list[3 - i]
        guessed_int = math.floor(guessed_int / 10)
    return guessed_list

def count_bulls_cows(secret, guess):
    bulls = 0
    j = 0
    for i in guess:
        if i == secret[j]:
            bulls += 1
        j += 1
    if bulls == 4:
        return 1
    cows = len(set(guess) & set(secret)) - bulls
    print_bulls_and_cows(bulls, cows)


def print_bulls_and_cows(b, c):
    if b == 0:
        print("There are no bulls.")
    elif b == 1:
        print("There is " + str(b) + " bull.")
    elif b > 1:
        print("There are " + str(b) + " bulls.")

    if c == 0:
        print("There are no cows.")
    elif c == 1:
        print("There is " + str(c) + " cow.")
    elif c > 1:
        print("There are " + str(c) + " cows.")
    print('-' * 45)


def print_win(n_of_attempts):
    print("Congratulations! Your guess #" + str(n_of_attempts) + " was correct.")
    print('-' * 45)
    print("((...))    " * 4)
    print("( O O )    " * 4)
    print(" \\   /     " * 4)
    print(" (`_`)     " * 4)
    print('-' * 45)


def main():
    print_hi()
    secret_num = [0, 0, 0, 0]
    num_of_attempts = 1
    initial(secret_num)

    while True:
        guess_num = take_input(num_of_attempts)
        if count_bulls_cows(guess_num, secret_num) == 1:
            print_win(num_of_attempts)
            return 0
        num_of_attempts += 1

if __name__ == "__main__":
    main()