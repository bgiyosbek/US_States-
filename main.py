import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()


found_states = []

# with open("50_states.csv") as states:
#     all_states = states["state"]

while len(found_states) < 50:
    answer_state = screen.textinput(title=f"Guess the States. {len(found_states)} / 50", prompt="What's  another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in found_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break




    if answer_state in all_states:
        found_states.append(answer_state)
        t = turtle.Turtle()
        t.color("black")
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


screen.exitonclick()