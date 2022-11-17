import random
import turtle


l = int(input("Enter the length: "))
dir = str(input("Choose a direction, enter 'l' for left and 'r' for right: "))
n = int(input("Enter the number of sides you need in the polygon: "))

s = turtle.getscreen()
t = turtle.Turtle()


def draw_polygon(n, l, dir):
    if l > 1:
        for i in range(n):
            t.forward(l)
            if dir == "l":
                t.left(360/n)
            elif dir == "r":
                t.right(360/n)
        draw_polygon(n,l*0.9, dir)


t.speed(100000)
# t.right(random.randint(0, 360))
for i in range(12):
    draw_polygon(n, l, dir)
    t.right(30)




input()
