import random
import turtle

s = turtle.getscreen()


t = turtle.Turtle()

t.left(random.randint(5,85))


def draw_square(x,dir):
    for i in range(4):
        t.forward(x)
        if dir == "l":
            t.left(90)
        elif dir == "r":
            t.right(90)

t.speed(1000000000)

for j in range(4):
    n = random.randint(50, 200)
    for i in range(n):
        t.forward(1)
        r = random.randint(0, 1)
        if r > 0.5:
            draw_square(i, "r")

    t.goto(0, 0)

    # n = random.randint(50, 200)
    # for i in range(n):
    #     t.forward(1)
    #     r = random.randint(0,1)
    #     if r>0.5:
    #         draw_square(i, "l")
    #
    # t.goto(0, 0)
    t.left(90)

input()
