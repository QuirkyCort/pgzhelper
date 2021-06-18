import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

r1 = Actor('square300')
r1.x = random.randint(100, 700)
r1.y = random.randint(100, 500)
r2 = Actor('square50')
r2.x = random.randint(100, 700)
r2.y = random.randint(100, 500)
r3 = Actor('square150')

mouse_pos = [0,0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def update():
    pass

def draw():
    screen.clear()

    r3.x = mouse_pos[0]
    r3.y = mouse_pos[1]

    r1.draw()
    r2.draw()
    r3.draw()

    if Collide.rect_rect(r1.x, r1.y, r1.width, r1.height, r3.x, r3.y, r3.width, r3.height):
        screen.draw.text("Red", (400,300), color='white')
    elif Collide.rect_rect(r2.x, r2.y, r2.width, r2.height, r3.x, r3.y, r3.width, r3.height):
        screen.draw.text("Blue", (400,300), color='white')

pgzrun.go() # Must be last line
