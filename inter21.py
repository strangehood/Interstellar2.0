from graph import *
import random as r

c = canvas()
windowSize(1000, 1000)
canvasSize(950, 1450)

# global vars:
xspeed = 0
yspeed = 0
star = None
x0 = 0
y0 = 0
x1 = 0
y1 = 0
rad = 0
star_tail = None
star_tail1 = None

brushColor("black")
rectangle(0, 0, 950, 1000)
brushColor("grey")
for i in range(500):
    high = r.randrange(1000)
    widht = r.randrange(1000)
    brushColor(randColor())
    penColor(randColor())
    circle(high, widht, 2)
label("ПА магите", 300, 440)
c = canvas()
penColor("grey")
brushColor("grey")
f1 = c.create_oval(273, 585, 298, 645, fill='grey', outline='grey')
f2 = c.create_oval(302, 585, 328, 645, fill='grey', outline='grey')
f3 = circle(285, 648, 12)
f4 = circle(317, 648, 12)
f5 = c.create_oval(273, 650, 295, 690, fill='grey', outline='grey')
f6 = c.create_oval(308, 650, 328, 690, fill='grey', outline='grey')
f7 = c.create_oval(310, 680, 350, 700, fill='grey', outline='grey')
f8 = c.create_oval(255, 680, 295, 700, fill='grey', outline='grey')

f9 = circle(300, 500, 25)
f10 = c.create_oval(310, 550, 370, 465, fill='grey', outline='grey')

f11 = circle(270, 535, 15)
f12 = circle(255, 537, 12)
f13 = circle(241, 543, 10)
f14 = circle(233, 552, 7)
f15 = circle(329, 538, 15)
f16 = circle(345, 535, 12)
f17 = circle(355, 525, 10)
f18 = circle(360, 515, 7)
penColor("white")
brushColor("white")
f19 = circle(310, 510, 20)


def legmovr():
    x = r.randrange(8)
    y = r.randrange(5)
    x1 = r.randrange(8)
    y1 = r.randrange(5)
    moveObjectTo(f1, 273 + x1 + x, 585 + y1 + y)
    moveObjectTo(f2, 302 + x1 + x, 585 + y1 + y)
    moveObjectTo(f3, 270 + x1 + x + 5, 630 + y1 + y + 5)
    moveObjectTo(f4, 300 + x1 + x + 5, 630 + y1 + y + 5)
    moveObjectTo(f5, 273 + x1 + x, 650 + y1 + y)
    moveObjectTo(f6, 308 + x1 + x, 650 + y1 + y)
    moveObjectTo(f7, 310 + x1 + x, 680 + y1 + y)
    moveObjectTo(f8, 255 + x1 + x, 680 + y1 + y)
    moveObjectTo(f9, 280 + x, 480 + y)
    moveObjectTo(f10, 280 + x, 520 + y)
    moveObjectTo(f11, 270 + x, 535 + y)
    moveObjectTo(f12, 255 + x, 537 + y)
    moveObjectTo(f13, 241 + x, 543 + y)
    moveObjectTo(f14, 233 + x, 552 + y)
    moveObjectTo(f15, 329 + x, 538 + y)
    moveObjectTo(f16, 345 + x, 535 + y)
    moveObjectTo(f17, 355 + x, 525 + y)
    moveObjectTo(f18, 360 + x, 515 + y)


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
    global x1, y1, rad, star_tail, star_tail1
    boom = None
    x1 += xspeed
    y1 += yspeed

    # star moving
    if star_tail is not None:
        deleteObject(star_tail)
    star_tail = line(x0, y0, x1, y1)
    moveObjectBy(star, xspeed, yspeed)
    chance = r.randint(1, 20)

    # star burst
    if chance == 1:
        if star_tail1 is not None:
            deleteObject(star_tail1)
        star_tail1 = line(x0, y0, x1, y1)
        deleteObject(star)
        deleteObject(star_tail)
        deleteObject(boom)
        star_generation()
        x1 = x0
        y1 = y0


onTimer(legmovr, 300)

brushColor("#A0522D")
penColor("#A0522D")
rectangle(500, 550, 1000, 950)
brushColor("#8B4513")
penColor("#8B4513")
rectangle(500, 550, 1000, 570)
rectangle(500, 640, 1000, 660)
rectangle(500, 720, 1000, 740)
rectangle(500, 820, 1000, 950)
brushColor("#B22222")
penColor("#B22222")
rectangle(500, 580, 520, 640)
book1 = rectangle(600, 580, 620, 640)
book4 = rectangle(800, 580, 820, 640)
rectangle(570, 660, 590, 720)
rectangle(770, 660, 790, 720)
book2 = rectangle(830, 660, 850, 720)
brushColor("#FFA500")
penColor("#FFA500")
book3 = rectangle(530, 580, 550, 640)
book5 = rectangle(630, 580, 650, 640)
rectangle(840, 580, 860, 640)
rectangle(600, 660, 620, 720)
book6 = rectangle(830, 660, 850, 720)
brushColor("#FF0000")
penColor("#FF0000")
circle(600, 790, 30)
brushColor("white")
penColor("white")
circle(600, 790, 25)
brushColor("black")
penColor("black")
l1 = line(600, 790, 600, 765)
l2 = line(600, 790, 620, 800)
brushColor("red")
penColor("red")
circle(620, 758, 10)
circle(582, 758, 10)


def linemv():
    a1 = r.randrange(13)
    b1 = r.randrange(13)
    moveObjectTo(l1, 600 + a1, 785 + b1)
    a2 = r.randrange(10)
    b2 = r.randrange(10)
    moveObjectTo(l2, 600 + a2, 785 + b2)


onTimer(linemv, 100)


def bookmv1():
    moveObjectBy(book1, 0, 4)
    moveObjectBy(book2, 0, 4)
    moveObjectBy(book3, 0, 4)


onTimer(bookmv1, 100)


def bookmv2():
    moveObjectBy(book4, 0, 2)
    moveObjectBy(book5, 0, 2)
    moveObjectBy(book6, 0, 2)


onTimer(bookmv2, 200)

star_generation()
x1 = x0
y1 = y0
onTimer(starfall, 200)    # works
run()