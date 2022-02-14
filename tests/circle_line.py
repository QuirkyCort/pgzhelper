import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

mouse_pos = [0, 0]
mouse_pressing = False

def on_mouse_move(pos):
    global mouse_pos
    if mouse_pressing:
        mouse_pos = pos
    
def on_mouse_down(pos):
    global mouse_pressing
    mouse_pressing = True

def on_mouse_up(pos):
    global mouse_pressing
    mouse_pressing = False
    
def update():
    pass

# l1x1 = 65  # random.randint(100, 700)
# l1y1 = 80  # random.randint(100, 500)
# l1x2 = l1x1  # random.randint(100, 700)
# l1y2 = 250  # andom.randint(100, 500)
l1x1 = random.randint(100, 400)
l1y1 = random.randint(100, 300)
l1x2 = l1x1+random.randint(100, 400)
l1y2 = l1y1#+random.randint(100, 400)
r    = 60 # random.randint(30, 150)
# c = [
#     120,  # random.randint(100, 700),
#     180, # mouse_pos[1],  # random.randint(100, 500),
#     r
# ]
        
def draw():
    # time.sleep(0.5)

    screen.clear()

    c = [
        mouse_pos[0],
        mouse_pos[1],
        r
    ]

    if Collide.circle_line(c[0], c[1], c[2], l1x1, l1y1, l1x2, l1y2):
        color = (255, 0, 0)
    else:
        color = (0, 255, 0)

    screen.draw.line((l1x1, l1y1), (l1x2, l1y2), color)
    screen.draw.circle((c[0], c[1]), c[2], color)

    ix, iy = Collide.line_circle_XY(l1x1, l1y1, l1x2, l1y2, c[0], c[1], c[2])
    if ix is not None:
        screen.draw.circle((l1x1, l1y1), 5, color='green')
        screen.draw.circle((ix, iy), 7, color='white')

pgzrun.go() # Must be last line
