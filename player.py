from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")
        self.color('green')

    def move_up(self):
        self.setheading(90)
        if self.ycor() >= 234:
            self.sety(275)
        elif self.ycor() >= 188:
            self.sety(234)
        elif self.ycor() >= 142:
            self.sety(188)
        elif self.ycor() >= 96:
            self.sety(142)
        elif self.ycor() >= 50:
            self.sety(96)
        elif self.ycor() >= 10:
            self.sety(50)
        else:
            self.forward(MOVE_DISTANCE)

    def move_back(self):
        self.setheading(270)
        if 234 < self.ycor() <= 275:
            self.sety(234)
        elif 188 < self.ycor() <= 234:
            self.sety(188)
        elif 142 < self.ycor() <= 188:
            self.sety(142)
        elif 96 < self.ycor() <= 142:
            self.sety(96)
        elif 50 < self.ycor() <= 96:
            self.sety(50)
        elif 0 < self.ycor() <= 50:
            self.sety(0)
        else:
            self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def log_jump_forward(self):
        self.setheading(90)
        self.forward(48)

    def log_jump_backward(self):
        self.setheading(270)
        self.forward(48)

    def on_your_mark(self):
        self.setheading(90)
        self.goto(STARTING_POSITION)
