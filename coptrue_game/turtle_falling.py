from turtle import Turtle
import random

class Randomly_Turtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shapes=('turtle','classic','circle','triangle','square')
        self.colors=('green','blue','white','red','white','orange')
        self.shapesizes=(0.5,1,2,3)
        self.create_turtle()

    def create_turtle(self):
        self.penup()
        self.shape(random.choice(self.shapes))
        self.color(random.choice(self.colors))
        self.shapesize(random.choice(self.shapesizes))
        self.goto(random.randint(-480,480),380)

    def move(self):
        self.goto(self.xcor(),self.ycor()-1)



