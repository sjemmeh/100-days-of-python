from art import logo
from replit import clear
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
start_game = input("Would you like to play a game of blackjack? Type 'y' or 'n': ").lower()
game_started = False
game_over = False
if start_game == 'y':
    game_started = True
winner = 0 # User = 1, Computer = 2
def draw_card(player, amount):
    """Draws a card on the defined player."""
    current_amount = 0
    while current_amount < amount:
        if player == "user":
            user.append(random.choice(cards))
            current_amount += 1
        else:
            computer.append(random.choice(cards))
            current_amount += 1


def new_game():
    """Resets the game state."""
    user.clear()
    computer.clear()
    draw_card("user", 2)
    draw_card("computer", 2)


def count_cards(player):
    """Counts the cards from a defined player."""
    count = 0
    if player == "user":
        for card in user:
            count += card
    else:
        for card in computer:
            count += card
    return count


while game_started:
    new_game()
    while game_over is not True:
        clear()
        print(logo)
        print(f"Your cards: {user}, score: {count_cards("user")}\nComputer's cards: {computer}, score: {count_cards("computer")}")
        another = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another == "y":
            draw_card("user", 1)
            if count_cards("user") > 21:
                game_over = True
                winner = 2
            else:
                draw_card("computer", 1)
                if count_cards("computer") > 21:
                    game_over = True
                    winner = 1
        else:
            draw_card("computer", 1)
            game_over = True
            if count_cards("computer") > 21:
                winner = 1
            else:
                if (count_cards("user") > count_cards("computer")):
                    winner = 1
                elif (count_cards("user") == count_cards("computer")):
                    winner = 0
                else:
                    winner = 2

    print(f"Your cards: {user}, final score: {count_cards("user")}\nComputer's cards: {computer}, final score: {count_cards("computer")} ")
    if winner == 0:
        print("A draw!")
    elif winner == 1:
        print("Congrats! You won!")
    else:
        print("Too bad! Dealer wins!")
    start_new_game = input("Would you like to try again? Type 'y' or 'n': ").lower()
    if start_new_game == "n":
        game_started = False
    else:
        game_over = False