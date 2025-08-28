from turtle import Screen
from one_paddle import Paddle , Display_and_game_over
from turtle_falling import Randomly_Turtle
import time

window=Screen()
window.bgcolor('black')
window.setup(1000,700)
window.title('coptrue game')
window.tracer(0)

paddle=Paddle()
new_turtle=Randomly_Turtle()
display=Display_and_game_over()

window.listen()

window.onkey(paddle.go_right,'Right')
window.onkey(paddle.go_left,'Left')

game_on=True
speed=0.005

while game_on:
    window.update()
    time.sleep(speed)

    new_turtle.move()

    #اذا تم الاتقاط new_turtle
    if paddle.distance(new_turtle) <50 and new_turtle.ycor() <-310:
        #الخسارة اذا تم التقاط سلحفة بيضاء
        if new_turtle.shape() == 'turtle' and new_turtle.pencolor() =='white':
            display.game_over()
            game_on=False
        else:    

            #زيادة الscoer حسب الشكل.
            if new_turtle.shape() == 'triangle':
                display.scoer=0
                speed=0.005
                display.updeta_and_display_scoer()

            elif new_turtle.shape() == 'turtle' and new_turtle.pencolor() != 'white':
                display.scoer+=5
                display.updeta_and_display_scoer()

            elif new_turtle.shape() == 'square':
                display.scoer+=2
                display.updeta_and_display_scoer()
                
            else:
                display.scoer+=1
                display.updeta_and_display_scoer()

        new_turtle.create_turtle()
        speed*=0.9

    #اذا لم يتم التقاط new_turtle

    if new_turtle.ycor()<-350:
        new_turtle.create_turtle()

    #منع المضرب من الخروج

    if paddle.xcor()+50 > 500  :
        paddle.setx(450)
        
    if paddle.xcor()-50 < -500:
        paddle.setx(-450)

window.exitonclick()