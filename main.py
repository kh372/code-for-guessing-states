import turtle
from os import write

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_state=[]


while len(guessed_state) <50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 state", prompt="What's another state name?").title()
    if answer_state:
        answer_state = answer_state.title()
    if answer_state == "Exit":
        remaining_states = [state for state in all_state not in guessed_state]
        new_data = pandas.DataFrame(remaining_states)
        new_data.to_csv("states_to_learn")
        break
    if answer_state in all_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)



turtle.mainloop()
