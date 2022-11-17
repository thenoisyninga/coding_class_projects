import random
import turtle
import math
import squares

print("Got here")

s = turtle.getscreen()
t = turtle.Turtle()
t.speed(100000000000)
for i in range(200):
    print(f"i ran {i} times")
    t.goto(i, 0)
    # t.circle(i)
    if (i % 6) == 0:
        test.draw_square(i)

for i in range(200):
    t.goto(-i, 0)
    # t.circle(i)
    if (i % 6) == 0:
        test.draw_square(i)

for i in range(200):
    t.goto(i, 0)
    # t.circle(-i)
    if (i % 6) == 0:
        test.draw_square(i)

for i in range(200):
    t.goto(-i, 0)
    # t.circle(-i)
    if (i % 6) == 0:
        test.draw_square(i)

input()

t.done()

