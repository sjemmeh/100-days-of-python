from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.


bidders = {}

bidding = True
while bidding:
    print(art.logo)
    name = input("What is your name? ")
    bid = float(input("What is your bid?: $"))
    bidders[name] = bid
    ask = input("Are there any other users who want to bid?: ").lower()
    if ask == "no":
        bidding = False
    clear()

current_winner = ""
current_bid = 0
for name in bidders:
    if current_bid < bidders[name]:
        current_winner = name
        current_bid = bidders[name]
print(art.logo)
print(f"Winner is {current_winner} with a bid of ${current_bid}.")