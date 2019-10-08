from graph import *
import random as r

windowSize(500, 500)
canvasSize(500, 500)

# global vars:
xspeed = 0
yspeed = 0
star = None


def star_generation():  # func generates random star
    global xspeed, yspeed, star

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
    xspeed = r.randint(4, 8) * r.choice([-1, 1])
    yspeed = r.randint(4, 8) * r.choice([-1, 1])

    # star drawing
    if (xspeed > 0) and (yspeed > 0):
        star = circle(0, 0, rad)
    elif (xspeed < 0) and (yspeed > 0):
        star = circle(500, 0, rad)
    elif xspeed > 0:
        star = circle(0, 500, rad)
    else:
        star = circle(500, 500, rad)


def starfall():  # func moves random star
    moveObjectBy(star, xspeed, yspeed)


star_generation()
onTimer(starfall, 100)
run()
