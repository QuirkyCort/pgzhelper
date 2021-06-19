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
for _ in range(10):
    x = random.randint(100, 700)
    y = random.randint(100, 500)
    lines.append([
        x,
        y,
        x + random.randint(10, 150),
        y + random.randint(10, 150),
    ])

def update(d):
    print(1 / d)

def draw():
    screen.clear()

    r1.draw()
    r2.draw()

    for l in lines:
        l[1] += 1
        l[3] += 1
        if l[1] > HEIGHT:
            l[1] -= 600
            l[3] -= 600
            l[0] = random.randint(100, 700)
            l[2] = random.randint(100, 700)
        screen.draw.line((l[0], l[1]), (l[2], l[3]), color='white')

    if Collide.obb_lines(r1.x, r1.y, w1, h1, r1.angle, lines) != -1:
        screen.draw.text('Yellow rect hit', (0,0), color='white')
    if Collide.obb_lines(r2.x, r2.y, w2, h2, r2.angle, lines) != -1:
        screen.draw.text('Cyan square hit', (0,100), color='white')

pgzrun.go() # Must be last line
