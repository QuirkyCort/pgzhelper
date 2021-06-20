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

c_r = 75

mouse_pos = [0,0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def update(d):
    pass

def draw():
    screen.clear()

    r1.draw()
    r2.draw()

    if Collide.obb_circle(r1.x, r1.y, w1, h1, r1.angle, mouse_pos[0], mouse_pos[1], c_r):
        color = (255, 255, 0)
    elif Collide.obb_circle(r2.x, r2.y, w2, h2, r2.angle, mouse_pos[0], mouse_pos[1], c_r):
        color = (0, 255, 255)
    else:
        color = (0, 55, 0)
    screen.draw.circle((mouse_pos[0], mouse_pos[1]), c_r, color)

pgzrun.go() # Must be last line
