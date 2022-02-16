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


r_w = 60
r_h = 30
r_a = 70

def obb_points(x, y, w, h, angle):
    half_w = w / 2
    half_h = h / 2
    r_angle = math.radians(angle)
    costheta = math.cos(r_angle)
    sintheta = math.sin(r_angle)

    wc = half_w * costheta
    hs = half_h * sintheta
    hc = half_h * costheta
    ws = half_w * sintheta
    points = [
        [x + wc + hs, y + hc - ws],
        [x - wc + hs, y + hc + ws],
        [x - wc - hs, y - hc + ws],
        [x + wc - hs, y - hc - ws],
    ]
    return points


mouse_pos = [0, 0]

def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_mouse_down(pos, button):
    global r_w, r_h
    if button == 4:
        r_w += 10
        r_h += 10
    if button == 5:
        r_w -= 10
        r_h -= 10


def update(d):
    r2.angle += 0.4
    r1.angle += 0.4

def draw():
    screen.clear()

    r1.draw()
    screen.draw.circle((r1.x, r1.y), 2, (255, 255, 0), 0)
    r2.draw()
    screen.draw.circle((r2.x, r2.y), 2, (0, 255, 255), 0)

    if Collide.obb_obb(r1.centerx, r1.centery, w1, h1, r1.angle, mouse_pos[0], mouse_pos[1], r_w, r_h, r_a):
        color = (255, 255, 0)
    elif Collide.obb_obb(r2.centerx, r2.centery, w2, h2, r2.angle, mouse_pos[0], mouse_pos[1], r_w, r_h, r_a):
        color = (0, 255, 255)
    else:
        color = (0, 255, 0)
    pts = obb_points(*mouse_pos, r_w, r_h, r_a)
    screen.draw.polygon(pts, color)


pgzrun.go()  # Must be last line
