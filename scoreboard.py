from turtle import *
from snake import *
from random import *


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = ..., undobuffersize: int = ..., visible: bool = ...
    ) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 225)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}", False, "center", ("Times New Roman", "16", "bold")
        )
