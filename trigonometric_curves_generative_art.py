import random
import turtle
import math

s = turtle.getscreen()
t = turtle.Turtle()
t.penup()
t.goto(-s.canvwidth, 0)
t.pendown()
t.speed(100000000000)
for j in range(360):
    # x = j
    # y = math.sin(math.radians(x)) * 100
    # t.goto(x - s.canvwidth, y)

    initial_y = random.randint(-500, 500)

    generatedNumber = random.randint(0, 100)
    if generatedNumber < 50:
        t.penup()
        t.goto(-250, initial_y)
        t.pendown()
        for i in range(720):
            x = i - 250
            y = (math.sin(math.radians(i)) * 100) + initial_y
            t.goto(x, y)
            print(x,y)
    else:
        t.penup()
        t.goto(-250, initial_y)
        t.pendown()
        for i in range(720):
            x = i - 250
            y = (math.cos(math.radians(i)) * 100) + initial_y
            t.goto(x, y)
            print(x,y)
t.circle(100)
# input()