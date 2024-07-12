from turtle import Screen, Turtle

turtle = Turtle()
count = 1


class OnScreen(Screen):
    def __init__(self):
        super().__init__()
        self.title(f"{count} / 50 || U.S. States Quiz Game")
        image = "blank_states_img.gif"
        self.addshape(image)
        turtle.shape(image)
