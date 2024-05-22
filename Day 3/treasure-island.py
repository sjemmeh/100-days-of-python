
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

active = True

while active:
    print("You are at a cross road. Where do you want to go? Type left or right.")
    direction = input()
    if direction == "left":
        print("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
        cross = input()
        if cross == "wait":
            print("You arrive at the island unharmed. Theres a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
            color = input()
            if color == "red":
                print("The moment you enter the room in engulfs in flames, you burn to death.")
                print("\n\nGame over. Try again!\n\n")
            elif color == "blue":
                print("The room appeared safe at first, but a large beast came from the closet, eating you alive.")
                print("\n\nGame over. Try again!\n\n")
            elif color == "yellow":
                print("The yellow door guides you to a room full of treasure, all for you to take!")
                print("You win!")
                active = False
            else:
                print("You open the door and suddenly lose consciousness. When you wake up you are locked up in a cage.")
                alive = False

        else:
            print("The current of the lake is strong, and the lake is full of aggressive trouts. You are eaten by the trouts.")
            alive = False
    else:
        print("The road you took was too dark to see proper and you fell into a dark hole.")
        print("\n\nGame over. Try again!\n\n")




