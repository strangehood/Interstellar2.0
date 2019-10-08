from graph import *
import random as r

windowSize(500, 500)
canvasSize(500, 500)

# global vars:
xspeed = 0
yspeed = 0
star = None
x0 = 0
y0 = 0
x1 = 0
y1 = 0


def star_generation():  # func generates random star
    global xspeed, yspeed, star, x0, y0

    # color generation:
    red = r.randint(155, 230)
    green = r.randint(155, 230)
    blue = r.randint(155, 230)
    penColor(red, green, blue)

    red = r.randint(155, 230)
    green = r.randint(155, 230)
    blue = r.randint(155, 230)
    brushColor(red, green, blue)

    # star size and speed generation:
    rad = r.randint(5, 10)
    xspeed = r.randint(8, 12) * r.choice([-1, 1])
    yspeed = r.randint(4, 6) * r.choice([-1, 1])

    # star drawing
    if (xspeed > 0) and (yspeed > 0):
        x0 = 0
        y0 = 0
        star = circle(y0, x0, rad)
    elif (xspeed < 0) and (yspeed > 0):
        x0 = 500
        y0 = 0
        star = circle(x0, y0, rad)
    elif (xspeed > 0) and (yspeed < 0):
        x0 = 0
        y0 = 500
        star = circle(0, 500, rad)
    else:
        x0 = 500
        y0 = 500
        star = circle(500, 500, rad)


def starfall():  # func moves random star
    global x1, y1
    star_tail = None
    x1 += xspeed
    y1 += yspeed
    deleteObject(star_tail)
    star_tail = line(x0, y0, x1, y1)
    moveObjectBy(star, xspeed, yspeed)



star_generation()
x1 = x0
y1 = y0
onTimer(starfall, 100)
run()
