from math import sqrt
import turtle
import random


win = turtle.Screen()
win.title("PONG")
win.bgcolor("cyan")
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a =0
score_b =0
win_Score =5



x=random.randint(-250, 250)
x2=random.randint(-250, 250)
x3=random.randint(-250, 250)
y=random.randint(-350, 350)
y2=random.randint(-350, 350)
y3=random.randint(-350, 350)



#add paddles and the ball

paddle_a = turtle.Turtle()
paddle_a.speed(3)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(3)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=-5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)



ball = turtle.Turtle()
ball.r=0.5  # type: ignore
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1  # type: ignore
ball.dy = -0.1  # type: ignore


obs1 = turtle.Turtle()
obs1.r2=0.5 # type: ignore
obs1.speed(0)
obs1.shape("circle")
obs1.color("blue")
obs1.penup()
obs1.goto(x, y)


obs2 = turtle.Turtle()
obs2.r2=0.5 # type: ignore
obs2.speed(0)
obs2.shape("circle")
obs2.color("green")
obs2.penup()
obs2.goto(x2, y2)


obs3 = turtle.Turtle()
obs3.r2=0.5 # type: ignore
obs3.speed(0)
obs3.shape("circle")
obs3.color("purple")
obs3.penup()
obs3.goto(x3, y3)




d=sqrt((ball.xcor()-obs1.xcor()) *(obs1.ycor()-obs1.ycor()))
z=sqrt((ball.xcor()-obs2.xcor()) *(obs2.ycor()-obs2.ycor()))


obstcls = [obs1, obs2, obs3]





pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)



#move the paddles
def paddle_a_up():
    y = paddle_a.ycor()
    y += 10
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 10
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

    #when a ball collides with an obsticale

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10



win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")




# main loop
while True:
    win.update()


    


     #move the ball
    ball.setx(ball.xcor() + ball.dx)  # type: ignore
    ball.sety(ball.ycor() + ball.dy)  # type: ignore
    
     #borders 
    if  ball.ycor() > 290:
         ball.sety(290)
         ball.dy *= -1  # type: ignore

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # type: ignore
        
        
    if ball.xcor() > 390:
        
        ball.goto(1, 1) 
        score_a +=1
        pen.clear()
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = 0.1 # type: ignore


    if ball.xcor() < -390:
        
        ball.goto(-1,-1)
        #ball.dx *= -1  # type: ignore
        score_b +=1
        ball.dx =0.1 # type: ignore
        pen.clear()
        pen.write("player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx = 0.1 # type: ignore

    for obs in obstcls:
    
        if obs.xcor() <-390:
            obs.setx(-390) 
        elif obs.xcor() > 390:
            obs.setx(390)
        
        if obs.ycor() > 290:
            obs.sety(290)
        elif obs.ycor() <-290:
            obs.sety(-290) 

    #set the borders for the paddles
    if paddle_a.ycor() > 240:
       paddle_a.sety(240)

    if paddle_a.ycor() < -240:
            paddle_a.sety(-240)
        
    if paddle_b.ycor() > 240:
       paddle_b.sety(240)

    if paddle_b.ycor() < -240:
            paddle_b.sety(-240)

        
        #collisions
    if  (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60 ):
            ball.setx( -340)
            ball.dx -= 0.1 # type: ignore
            ball.dx *= -1  # type: ignore
         

    if  (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ):
            ball.setx(340)
            ball.dx += 0.1 # type: ignore
            ball.dx *= -1  # type: ignore
         
        


    if is_collided_with(ball,obs2):
            ball.goto(ball.xcor(), ball.ycor())  # type: ignore
            ball.dx *=-1 #type: ignore
            ball.dy*=-1 #type: ignore


    if is_collided_with(ball,obs1):
            ball.goto(ball.xcor(), ball.ycor())  # type: ignore
            ball.dx *=-1 #type: ignore
            ball.dy*=-1 #type: ignore

        #accelerate and change direction of the  ball after coliding with obs3
    if is_collided_with(ball,obs3):
            ball.goto(ball.xcor(), ball.ycor())  # type: ignore
            ball.dx *=-1 #type: ignore
            ball.dy*=-1 #type: ignore
            ball.dx +=1 #type: ignore


    

        
    #AI Player
    


    if (paddle_a.ycor() < ball.ycor()) and abs(paddle_a.ycor() - ball.ycor()) > 10:
        paddle_a_up()

    elif (paddle_a.ycor() > ball.ycor()) and abs(paddle_a.ycor() - ball.ycor()) > 10:
        paddle_a_down()

    


    


    if (score_a ==win_Score or score_b == win_Score):
        pen2.write("Game Over", move=True, align="center", font=("Comic Sana", 40, "bold"))
        pen2.goto(400, 300)
        break

    

