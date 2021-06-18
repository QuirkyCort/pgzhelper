import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

circles = []
for _ in range(5):
    circles.append([
        random.randint(100, 700),
        random.randint(100, 500),
        random.randint(10, 200)
    ])

mouse_pos = [0,0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def update():
    pass

def draw():
    screen.clear()


    for c in circles:
        if Collide.circle_point(c[0], c[1], c[2], mouse_pos[0], mouse_pos[1]):
            color = (255, 0, 0)
        else:
            color = (0, 255, 0)
        screen.draw.circle((c[0], c[1]), c[2], color)

pgzrun.go() # Must be last line
