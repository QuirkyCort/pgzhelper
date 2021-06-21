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

lines = []
for _ in range(100):
    lines.append([
        random.randint(100, 700),
        random.randint(100, 500),
        random.randint(-150, 150),
        random.randint(-150, 150),
    ])

def update(d):
    print(1 / d)

def draw():
    screen.clear()

    r1.draw()
    r2.draw()

    for l in lines:
        l[1] += 1
        if l[1] > HEIGHT:
            l[1] = 0
            l[0] = random.randint(100, 700)

        if Collide.obb_line(r1.x, r1.y, w1, h1, r1.angle, l[0], l[1], l[0]+l[2], l[1]+l[3]):
            color = (255, 255, 0)
            ix, iy = Collide.line_obb_XY(l[0], l[1], l[0]+l[2], l[1]+l[3], r1.x, r1.y, w1, h1, r1.angle)
            screen.draw.circle((l[0], l[1]), 5, color='green')
            screen.draw.circle((ix, iy), 7, color='white')
        elif Collide.obb_line(r2.x, r2.y, w2, h2, r2.angle, l[0], l[1], l[0]+l[2], l[1]+l[3]):
            color = (0, 255, 255)
            ix, iy = Collide.line_obb_XY(l[0], l[1], l[0]+l[2], l[1]+l[3], r2.x, r2.y, w2, h2, r2.angle)
            screen.draw.circle((l[0], l[1]), 5, color='green')
            screen.draw.circle((ix, iy), 7, color='white')
        else:
            color = (0, 55, 0)
        screen.draw.line((l[0], l[1]), (l[0]+l[2], l[1]+l[3]), color)

pgzrun.go() # Must be last line
