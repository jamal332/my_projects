from turtle import Turtle 

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(1,5)
        self.goto(0,-320)

    def go_right(self):
        self.goto(x=self.xcor()+60,y=self.ycor())

    def go_left(self):
        self.goto(x=self.xcor()-60,y=self.ycor())



class Display_and_game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0,250)
        self.scoer=0
        self.sam=Turtle()
        self.sam.hideturtle()
        self.write(f'Scoer: {self.scoer}',align='center',font=('arial',20,'normal'))

    def updeta_and_display_scoer(self):
        self.clear()
        self.write(f'Scoer: {self.scoer}',align='center',font=('arial',20,'normal'))

    def game_over(self):
        self.sam.hideturtle()
        self.sam.penup()
        self.sam.goto(0,0)
        self.sam.color('white')
        self.sam.write('Game Over',align='center',font=('arial',40,'normal'))