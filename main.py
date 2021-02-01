import turtle as t
import pandas

screen = t.Screen()
screen.setup(width=700, height=500)
image = "./blank_states_img.gif"
screen.addshape(image)
t.shape(image)


def create_text(x_pos, y_pos, place):
    loc_turtle = t.Turtle()
    loc_turtle.hideturtle()
    loc_turtle.penup()
    loc_turtle.setposition(x=x_pos, y=y_pos)  # Set Position First Before writing
    loc_turtle.write(arg=place, move=True, align="center", font=("Arial", 10, "normal"))


game_is_on = True
number_of_states = 0
while game_is_on:
    states = pandas.read_csv("50_states.csv")
    answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
    for state in states["state"]:
        if state.lower() == answer_state.lower():
            location = states[states["state"] == answer_state]  # Get the row of the state
            print(location)
            create_text(x_pos=location["x"].item(), y_pos=location["y"].item(), place=state)
            number_of_states += 1
            screen.title(f"({number_of_states}/50) U.S What State?")
            if number_of_states == 50:
                game_is_on = False
