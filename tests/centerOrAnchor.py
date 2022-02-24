import pgzrun
import math
from pgzhelper import *

WIDTH=800
HEIGHT=600

r = Actor('square150')

FIREBALL_RADIUS = 7
fireball = Actor('fireball1', anchor=(54, 32))
fireball.images = ['fireball1','fireball2','fireball3','fireball4']
fireball.fps = 10
fireball.radius = FIREBALL_RADIUS

radius = 50
angle = 0

c_r = 50

mouse_pos = [0,0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def update():
    global angle

    angle += 0.01
    fireball.x = radius * math.cos(angle) + 400
    fireball.y = radius * math.sin(angle) + 300
    fireball.angle = angle / math.pi * -180 - 90
    fireball.animate()

def draw():
    screen.clear()

    fireball.draw()
    screen.draw.line((400,300), (fireball.x, fireball.y), (255,255,255))
    screen.draw.circle((fireball.x, fireball.y), FIREBALL_RADIUS, (255,255,255))
    screen.draw.circle((fireball.center[0], fireball.center[1]), FIREBALL_RADIUS, (255,255,255))

    r.x = mouse_pos[0]
    r.y = mouse_pos[1]
    r.draw()
    
    if fireball.circle_colliderect(r):
        screen.draw.text("hit", (400,300), color='white')

pgzrun.go() # Must be last line
