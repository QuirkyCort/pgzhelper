import pgzrun
from pgzhelper import *

WIDTH=800
HEIGHT=600

tank = Actor('tank', anchor=(56, 48))
tank.x = 400
tank.y = 300
tank.collision_width = 109
tank.collision_height = 100

obs1 = Actor('square150', anchor=(0,0))
obs1.angle = 45
obs1.x = 100
obs1.y = 100

obs2 = Actor('square150')
obs2.angle = 0
obs2.x = 600
obs2.y = 500


def update():
    orig_x, orig_y, orig_angle = tank.x, tank.y, tank.angle

    if keyboard.up:
        tank.move_forward(1)
    elif keyboard.down:
        tank.move_back(1)
    elif keyboard.left:
        tank.angle += 1
    elif keyboard.right:
        tank.angle -= 1

    for obs in [obs1, obs2]:
        if tank.obb_collideobb(obs):
            tank.x, tank.y, tank.angle = orig_x, orig_y, orig_angle
            break

def draw():
    screen.fill((0,100,0))

    obs1.draw()
    obs2.draw()
    tank.draw()

pgzrun.go() # Must be last line
