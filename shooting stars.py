from graph import *
import random as r

def star_generation():
    global star_number
    star_number = r.randint(1, 4)


def starfall():
    if star_list == []:
        star_generation()


star_number = None
star_list = []
star_generation()
onTimer(starfall, 1000)
run()