import pgzrun
import random
from pgzhelper import Collide

WIDTH = 800
HEIGHT = 600

l1x1 = random.randint(300, 700)
l1y1 = random.randint(300, 500)
l1x2 = random.randint(100, 200)
l1y2 = random.randint(100, 200)
radius = random.randint(10, 150)
c = [
    random.randint(100, 700),
    random.randint(100, 500),
]

mouse_pos = [0, 0]
def on_mouse_move(pos):
    global mouse_pos
    mouse_pos = pos

def on_mouse_down(pos, button):
    global radius
    if button == 4:
        radius += 10
    if button == 5:
        radius -= 10

def update():
    pass

def draw():
    screen.clear()
    c[0] = mouse_pos[0]
    c[1] = mouse_pos[1]

    if Collide.circle_line(c[0], c[1], radius, l1x1, l1y1, l1x2, l1y2):
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)
        
    screen.draw.line((l1x1, l1y1), (l1x2, l1y2), color)
    screen.draw.circle((c[0], c[1]), radius, color)

    ix, iy = Collide.line_circle_XY(l1x1, l1y1, l1x2, l1y2, c[0], c[1], radius)

    if ix is not None:
        screen.draw.circle((l1x1, l1y1), 5, color='green')
        screen.draw.circle((ix, iy), 7, color='white')

pgzrun.go()  # Must be last line
