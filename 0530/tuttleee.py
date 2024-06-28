import turtle
import random

def random_color() :
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)
def random_go() :
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    return (x,y)


screen = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.pensize(30)
t.speed(2)
t.pendown
t.shapesize(10, 10)
for turtle i n range (5):
    t.pencolor(random_color())
    for turtle in range (2):
        t.goto(random_go())
        t.color(random_color())
        
        
    
    
