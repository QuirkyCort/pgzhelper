import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

def update():
    pass

def draw():
    time.sleep(0.5)

    screen.clear()

    c = [
        random.randint(100, 700),
        random.randint(100, 500),
        random.randint(10, 150)
    ]

    l1x1 = random.randint(100, 700)
    l1y1 = random.randint(100, 500)
    l1x2 = random.randint(100, 700)
    l1y2 = random.randint(100, 500)

    if Collide.circle_line(c[0], c[1], c[2], l1x1, l1y1, l1x2, l1y2):
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)

    screen.draw.line((l1x1, l1y1), (l1x2, l1y2), color)
    screen.draw.circle((c[0], c[1]), c[2], color)

    ix, iy = Collide.line_circle_XY(l1x1, l1y1, l1x2, l1y2, c[0], c[1], c[2])
    if ix is not None:
        screen.draw.circle((l1x1, l1y1), 5, color='green')
        screen.draw.circle((ix, iy), 7, color='white')

pgzrun.go() # Must be last line
