import turtle
import pandas

screen = turtle.Screen()
screen.title("Provincie Spel")
screen.bgpic("provincies.png")
screen.setup(909, 1024)
screen.cv._rootwindow.resizable(False, False) # Annoying AF

data = pandas.read_csv("12_provincies.csv")
states = data.provincie.to_list()
amount_of_states = len(states)
guessed_states = []

while len(guessed_states) < amount_of_states:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{amount_of_states} geraden", prompt="Welke provincie wil je raden?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Provincies_te_leren.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        state_data = data[data.provincie == answer_state]
        text.goto(state_data.x.item(), state_data.y.item())
        text.write(state_data.provincie.item())

if len(guessed_states) == amount_of_states:
    print("Goedzo! Je hebt alle procincies geraden!")

# def get_mouse_click_coor(x, y):
#     print(f"{int(x)},{int(y)}")
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()