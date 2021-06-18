import pgzrun
import random
from pgzhelper import *
import time

WIDTH=800
HEIGHT=600

def update():
    pass

def draw():
    screen.clear()
    time.sleep(0.5)

    circle = [
        random.randint(100, 700),
        random.randint(100, 500),
        random.randint(10, 150)
    ]

    points = []
    for _ in range(10):
        points.append([
            random.randint(100, 700),
            random.randint(100, 500)
        ])
    
    for p in points:
        screen.draw.filled_circle((p[0], p[1]), 2, (255, 255, 255))

    if Collide.circle_points(circle[0], circle[1], circle[2], points) != -1:
        color  = (255, 0, 0)
    else:
        color = (0, 255, 0)
    screen.draw.circle((circle[0], circle[1]), circle[2], color)

pgzrun.go() # Must be last line
