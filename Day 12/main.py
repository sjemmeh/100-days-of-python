#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from replit import clear
import random
def start_game():
    game_started = False
    def game(count):
        game_started = True
        guesses = count
        random_number = random.randint(1, 100)
        while guesses > 0 and game_started:
            print(f"You have {guesses} remaining to guess the number")
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == random_number:
                print(f"You guessed the number!")
                game_started = False
            elif guess < random_number:
                print("Too low!")
                guesses -= 1
            elif guess > random_number:
                print("Too high!")
                guesses -= 1
        if guesses == 0:
            print("You lose! Would you like to try again?")
            again = input("Y/N: ").lower()
            if again == "y":
                start_game()



    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking ofa number between 1 and 100.")
    valid_input = False
    while not valid_input:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            valid_input = True
            game(10)
        elif difficulty == "hard":
            valid_input = True
            game(5)

start_game()