import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

r1 = Actor('rect200')
r2 = Actor('square150')
w1 = r1.width
h1 = r1.height
w2 = r2.width
h2 = r2.height

r1.x = random.randint(100, 700)
r1.y = random.randint(100, 500)
r1.angle = random.randint(0, 359)
r2.x = random.randint(100, 700)
r2.y = random.randint(100, 500)
r2.angle = random.randint(0, 359)

points = []
for _ in range(40):
    points.append([
        random.randint(100, 700),
        random.randint(100, 500)
    ])

def update():
    pass

def draw():
    screen.clear()

    r1.draw()
    r2.draw()

    for p in points:
        p[1] += 1
        if p[1] > HEIGHT:
            p[1] = 0
            p[0] = random.randint(100, 700)

        if Collide.obb_point(r1.x, r1.y, w1, h1, r1.angle, p[0], p[1]):
            color = (255, 255, 0)
        elif Collide.obb_point(r2.x, r2.y, w2, h2, r2.angle, p[0], p[1]):
            color = (0, 255, 255)
        else:
            color = (0, 55, 0)
        screen.draw.filled_circle((p[0], p[1]), 2, color)

pgzrun.go() # Must be last line
