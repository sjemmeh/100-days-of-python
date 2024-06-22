import random

from art import logo
from art import vs
from game_data import data
from replit import clear

# Get amount of questions
QUESTION_AMOUNT = len(data)-1
# Fill aray with all question numbers
def random_account():
    """Get random account"""
    return random.randint(0, QUESTION_AMOUNT)

def ask_question(score):
    option1 = random_account()
    option2 = random_account()
    while option1 == option2: # Making sure we never get the same question
        option1 = random_account()
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {data[option1]['name']}, a {data[option1]['description']}, from {data[option1]['country']}")
    print(vs)
    print(f"Against B: {data[option2]['name']}, a {data[option2]['description']}, from {data[option2]['country']}")
    ask = input("Who has more followers? Type 'A' or 'B': ")
    if ask == "A":
        if data[option1]['follower_count'] > data[option2]['follower_count']:
            return True
        else:
            return False
    if ask == "B":
        if data[option2]['follower_count'] > data[option1]['follower_count']:
            return True
        else:
            return False

def game_start():
    score = 0
    game_over = False
    while not game_over:
        clear()
        print(logo)
        if ask_question(score):
            score += 1
        else:
            game_over = True
            print(f"Sorry, that's not right. Final score: {score}")


game_start()