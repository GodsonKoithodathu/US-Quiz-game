from turtle import Turtle

FONT = "Courier", 6, "bold"


class WriteOnMap(Turtle):
    def __init__(self, state_name, answer):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(state_name.x.iloc[0], state_name.y.iloc[0])
        self.write(arg=answer, align='center', font=FONT)
