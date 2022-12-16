#https://www.patreon.com/posts/45998588
# https://docs.python.org/3/library/turtle.html
#https://www.youtube.com/watch?v=bzWzlXiavXs

# import libraries
# turtle is library for graphics
import turtle

# shorten the turtle to Ttl for time purposes
from turtle import Turtle as Ttl
# import random for the function of the food
import random
# import time for the snake and fruit
import time
# import os for the image import
import os
# import settings to keep the game running
from settings import *

# this opens the game folder file
game_folder = os.path.dirname(__file__)

bgimg = os.path.join(game_folder, 'jets logo.png')
football = os.path.join(game_folder, 'football.gif')

#this creates the screen alon with putting the jets logo as the background
screen = turtle.Screen()
screen.title('SNAKE GAME')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('green')
# specifically uses image as background for game
screen.bgpic(bgimg)

#makes the border for the snake to stay in

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# creates the snake and gives it its values

s = Ttl()
s.speed(0)
s.shape('square')
s.color("black")
s.penup()
s.goto(0,0)
s.dir = 'stop'

# turns the food it eats into footballs
screen.addshape(football)

# create
fruit = Ttl()
fruit.speed(0)
turtle.register_shape(football)
fruit.shape(football)
#makes the fruit as the football along with its size
fruit.penup()
fruit.goto(30,30)


#does the scoring along with its placement on the screen
scoring = Ttl()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("Score :",align="center",font=("Courier",24,"bold"))


# does the movement of the snake, a version of an if statement because if it is going one way it can only go the other

def s_down():
    if s.dir != (0,1):
        s.dir = (0,-1)
def s_up():
    if s.dir != (0,-1):
        s.dir = (0,1)
def s_left():
    if s.dir != (1,0):
        s.dir = (-1,0)
def s_right():
    if s.dir != (-1,0):
        s.dir = (1,0)

# this describes how the snake will move and how fast it moves is based off of previous code
def s_move():
    if s.dir == (0,-1):
        y = s.ycor()
        s.sety(y - SNAKE_SPEED)
    
    if s.dir == (0,1):
        y = s.ycor()
        s.sety(y + SNAKE_SPEED)
    
    if s.dir == (-1,0):
        x = s.xcor()
        s.setx(x - SNAKE_SPEED)
    
    if s.dir == (1,0):
        x = s.xcor()
        s.setx(x + SNAKE_SPEED)

# input....

screen.listen()
screen.onkeypress(s_up, "Up")
screen.onkeypress(s_down, "Down")
screen.onkeypress(s_left, "Left")
screen.onkeypress(s_right, "Right")

# game loop

while True:
    screen.update()

    if s.distance(fruit)< 20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        SCORE+=1
        scoring.write("Score:{}".format(SCORE),align="center",font=("Courier",24,"bold"))
        DELAY-=0.001
        
        ## creating new_ball
        new_fruit = Ttl()
        new_fruit.speed(0)
        new_fruit.shape(football)
        # new_fruit.color('red')
        new_fruit.penup()
        eaten_fruit.append(new_fruit)
    # sets eaten fruit coords
    for index in range(len(eaten_fruit)-1,0,-1):
        a = eaten_fruit[index-1].xcor()
        b = eaten_fruit[index-1].ycor()
        
        eaten_fruit[index].goto(a,b)
    # makes eaten fruit follow snake if any is eaten
    if len(eaten_fruit) > 0:
        a = s.xcor()
        b = s.ycor()
        eaten_fruit[0].goto(a,b)

    s_move()

    if s.xcor() > 280 or s.xcor() < -300 or s.ycor()>240 or s.ycor()<-240:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('turquoise')
        scoring.goto(0,0)
        scoring.write("   GAME OVER \n Your Score is {}".format(SCORE),align="center",font=("Courier",30,"bold"))


            ## snake collision
    for food in eaten_fruit:
        if food.distance(s) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('turquoise')
            scoring.goto(0,0)
            scoring.write("    GAME OVER \n Your Score is {}".format(SCORE),align="center",font=("Courier",30,"bold"))


    time.sleep(DELAY)


turtle.Terminator()

