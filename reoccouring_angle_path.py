import math
import random
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def draw_square(x,dir):
    for i in range(4):
        t.forward(x)
        if dir == "l":
            t.left(90)
        elif dir == "r":
            t.right(90)

intital_value = 0
step = 0.5
limit = 30

t.speed(1000)

increasing = True

t.penup()
t.goto(-500,0)
t.pendown()

while True:
    print(intital_value)
    t.left(intital_value)
    t.forward(5)
    if intital_value != 0:
        rad = (100/intital_value) * 10
        if abs(rad) > 2:
            draw_square(rad, 'r')
            # t.circle(rad)
    if increasing:
        intital_value += step
    else:
        intital_value -= step
    if intital_value >= limit:
        increasing = False
    if intital_value <= -limit:
        increasing = True


