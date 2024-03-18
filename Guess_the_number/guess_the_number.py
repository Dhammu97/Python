from random import randint
from art import logo
 
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_ans(ans, guess,turns):
    if guess > ans:
        print("Too High! Guess another")
        return turns-1
    elif guess < ans:
        print("Too Low! Guess another")
        return turns-1
    else:
        print(f"you got it! the answer was {ans}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS


 
def game():

    print(logo)
    print("Welcome to the Number Guessing Game!")

    print("I'm thinking of a number between 1 and 100.")

    ans = randint(1, 100)
    turns = set_difficulty()

    guess=0
    while ans != guess:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        turns = check_ans(ans, guess, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return 
        elif guess != ans:
            print("Guess again.")

game()
