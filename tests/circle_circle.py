import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

c = [
    random.randint(100, 700),
    random.randint(100, 500),
    random.randint(10, 150)
]

c2_r = 75

mouse_pos = [0,0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def update():
    pass

def draw():
    screen.clear()

    if Collide.circle_circle(c[0], c[1], c[2], mouse_pos[0], mouse_pos[1], c2_r):
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)

    screen.draw.circle((c[0], c[1]), c[2], color)
    screen.draw.circle((mouse_pos[0], mouse_pos[1]), c2_r, color)


pgzrun.go() # Must be last line
