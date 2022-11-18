from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(0, 258)
        self.pencolor("white")
        self.level = 1
        self.write(f"Level: {self.level}", move=False, align=ALIGN, font=FONT)

    def pass_level(self):
        self.clear()
        self.setposition(0, 258)
        self.write(f"Level: {self.level}", move=False, align=ALIGN, font=FONT)
        self.setposition(0, -20)
        self.write(f"Nice Job!", move=False, align=ALIGN, font=FONT)
        time.sleep(3)
        self.clear()
        self.level += 1
        self.setposition(0, 258)
        self.write(f"Level: {self.level}", move=False, align=ALIGN, font=FONT)

    def beat_game(self):
        self.level -= 1
        self.clear()
        self.setposition(0, 258)
        self.write(f"Level: {self.level}", move=False, align=ALIGN, font=FONT)
        self.setposition(0, -20)
        self.write(f'Congratulations! You have proven\nthat turtles are better than frogs!', move=False, align=ALIGN,
                   font=("Courier", 12, "normal"))

    def game_over(self):
        self.setposition(0, -20)
        self.write(f"Game Over", move=False, align=ALIGN, font=FONT)

    def reset_board(self):
        self.clear()
        self.level = 1
        self.setposition(0, 258)
        self.write(f"Level: {self.level}", move=False, align=ALIGN, font=FONT)
