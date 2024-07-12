import pandas
from writing import WriteOnMap
from turtle import Turtle, Screen

# Creating some empty list:
correct_guess = []
missed_states = []
# initializing the turtle module:
turtle = Turtle()
screen = Screen()

# Below line of code can get u "x & Y" cor when u click on screen:
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

# This line of code is for reading the data from the "50 states csv" file:
data = pandas.read_csv('50_states.csv')
# getting hold of the states column and saving it in the form of the list:
all_states = data.state.to_list()

while len(correct_guess) < 50:
    # setting the screen for the game:
    screen.title(f"{len(correct_guess)} / 50 || U.S. States Quiz Game")
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)
    # getting hold of the user's input:
    user_answer = screen.textinput(title="Guess the state", prompt="Enter the name of the States?").title()
    # this will exit the while loop and add all the remaining states that user has missed to guess:
    if user_answer == 'Exit':
        missed_states = [state for state in all_states if state not in correct_guess]
    #     for state in all_states:
    #         if state not in correct_guess:
    #             missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv('States to learn.csv')
        break

    # this for loop will go through all the list and search for the user's choice and set hold of X and Y coor:
    for name in all_states:
        if user_answer == name:
            state_name = (data[data.state == name])
            WriteOnMap(state_name, user_answer)
            correct_guess.append(user_answer)
