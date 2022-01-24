from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        # self.shapesize(stretch_wid=2, stretch_len=2)
        # self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.move_x
        new_ycor = self.ycor() + self.move_y
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1
        self.move_speed *= 0.9

    def misses_paddle(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.move_x *= -1
