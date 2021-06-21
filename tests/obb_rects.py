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

rects = []
for _ in range(10):
    rects.append([
        random.randint(100, 700),
        random.randint(0, 600),
        random.randint(10, 50),
        random.randint(10, 50)
    ])

def update(d):
    print(1 / d)

def draw():
    screen.clear()

    r1.draw()
    r2.draw()

    for r in rects:
        r[1] += 1
        if r[1] > HEIGHT:
            r[1] -= 600
            r[0] = random.randint(100, 700)
            r[2] = random.randint(10, 50)
            r[3] = random.randint(10, 50)
        screen.draw.rect(Rect(r[0] - r[2] / 2, r[1] - r[3] / 2, r[2], r[3]), color='white')

    if Collide.obb_rects(r1.x, r1.y, w1, h1, r1.angle, rects) != -1:
        screen.draw.text('Yellow rect hit', (0,0), color='white')
    if Collide.obb_rects(r2.x, r2.y, w2, h2, r2.angle, rects) != -1:
        screen.draw.text('Cyan square hit', (0,100), color='white')

pgzrun.go() # Must be last line
