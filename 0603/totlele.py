

import turtle
import random

        
    
def random_color() :    
    r = random.random()
    g = random.random()
    b = random.random()
    return (r,g,b)

def draw_square(t):
    t.color(random_color())
    t.pendown()
    for turtle in range(4):
        t.forward(100)  
        t.right(90)
    t.penup()


t = turtle.Turtle()
t.shape("turtle")
t.pensize(60)
t.speed(10)

window = turtle.Screen()
window.title("Turtle Graphics with Random Colors")
window.bgcolor("white")


t.penup()

t.goto(-400,300)
draw_square(t)
t.goto(-200,300)
draw_square(t)
t.goto(-0,300)
draw_square(t)
t.goto(-400,100)
draw_square(t)
t.goto(-200,100)
draw_square(t)
t.goto(-0,100)
draw_square(t)
t.goto(-400,-100)
draw_square(t)
t.goto(-200,-100)
draw_square(t)
t.goto(-0,-100)
draw_square(t)

window.mainloop()

