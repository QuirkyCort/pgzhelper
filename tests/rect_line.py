import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

r1 = Actor('rect200')
r2 = Actor('square150')

def update():
    pass

def draw():
    time.sleep(1)

    screen.clear()

    r1.x = random.randint(100, 700)
    r1.y = random.randint(100, 500)
    r2.x = random.randint(100, 700)
    r2.y = random.randint(100, 500)

    lines = []
    for _ in range(5):
        x1 = random.randint(100, 700)
        y1 = random.randint(100, 500)
        l = random.randint(5, 20)
        x2 = x1 + l * random.choice([-1, 1])
        l = random.randint(5, 20)
        y2 = y1 + l * random.choice([-1, 1])
        lines.append([x1, y1, x2, y2])

    for _ in range(5):
        x1 = random.randint(100, 700)
        y1 = random.randint(100, 500)
        l = random.randint(100, 300)
        x2 = x1 + l * random.choice([-1, 1])
        l = random.randint(100, 300)
        y2 = y1 + l * random.choice([-1, 1])
        lines.append([x1, y1, x2, y2])

    r1.draw()
    r2.draw()

    for l in lines:
        if Collide.rect_line(r1.x, r1.y, r1.width, r1.height, l[0], l[1], l[2], l[3]):
            color = (255, 255, 0)
        elif Collide.rect_line(r2.x, r2.y, r2.width, r2.height, l[0], l[1], l[2], l[3]):
            color = (0, 255, 255)
        else:
            color = (0, 255, 0)
        screen.draw.line((l[0], l[1]), (l[2], l[3]), color)

pgzrun.go() # Must be last line
