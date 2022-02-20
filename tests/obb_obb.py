import pgzrun
import random
from pgzhelper import *

WIDTH = 800
HEIGHT = 600

# r1 = Actor('rect200', anchor=("left", "bottom"))
r1 = Actor('rect200', anchor=(7.5, 30))
r2 = Actor('square150', anchor=(130, 80))
w1 = r1.width
h1 = r1.height
w2 = r2.width
h2 = r2.height

r1.x = random.randint(100, 300)
r1.y = random.randint(100, 500)
r1.angle = random.randint(0, 359)
r2.x = random.randint(400, 700)
r2.y = random.randint(100, 500)
r2.angle = random.randint(0, 359)

r3 = Actor('square50')
r3_w = 50
r3_h = 50

def on_mouse_move(pos):
    r3.x = pos[0]
    r3.y = pos[1]

def on_mouse_down(pos, button):
    global r3_w, r3_h
    if button == 4:
        r3.scale *= 1.1
        r3_w *= 1.1
        r3_h *= 1.1
    if button == 5:
        r3.scale *= 0.9
        r3_w *= 0.9
        r3_h *= 0.9


def update(d):
    r2.angle += 0.2
    r1.angle += 0.2
    r3.angle -= 0.3

def draw():
    screen.clear()

    r1.draw()
    screen.draw.circle((r1.x, r1.y), 2, (255, 255, 0))
    r2.draw()
    screen.draw.circle((r2.x, r2.y), 2, (0, 255, 255))
    r3.draw()

    if Collide.obb_obb(r1.centerx, r1.centery, w1, h1, r1.angle, r3.x, r3.y, r3_w, r3_h, r3.angle):
        screen.draw.text('Yellow rect hit', (0,0), color='white')
    elif Collide.obb_obb(r2.centerx, r2.centery, w2, h2, r2.angle, r3.x, r3.y, r3_w, r3_h, r3.angle):
        screen.draw.text('Cyan square hit', (0,100), color='white')


pgzrun.go()  # Must be last line
