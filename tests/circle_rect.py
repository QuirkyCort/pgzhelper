import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

r1 = Actor('rect200')
r1.x = random.randint(100, 700)
r1.y = random.randint(100, 500)

r2 = Actor('square150')
r2.x = random.randint(100, 700)
r2.y = random.randint(100, 500)

c2_r = 75

mouse_pos = [0,0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def update():
    pass

def draw():
    screen.clear()

    if Collide.circle_rect(mouse_pos[0], mouse_pos[1], c2_r, r1.x, r1.y, r1.width, r1.height):
        color = (255, 255, 0)
    elif Collide.circle_rect(mouse_pos[0], mouse_pos[1], c2_r, r2.x, r2.y, r2.width, r2.height):
        color = (0, 255, 255)
    else:
        color = (0, 255, 0)

    r1.draw()
    r2.draw()
    screen.draw.circle((mouse_pos[0], mouse_pos[1]), c2_r, color)

pgzrun.go() # Must be last line
