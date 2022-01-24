from turtle import Turtle

turtle = Turtle()


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.paddle(xcor, ycor)

    def paddle(self, xcor, ycor):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(xcor, ycor)

    def go_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def go_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
