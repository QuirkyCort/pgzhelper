import pgzrun
from pgzhelper import *

alien = Actor('alien_walk1')
alien.images = ['alien_walk1', 'alien_walk2']
alien.fps = 3

alien2 = Actor('alien_walk1')
alien2.load_images('alien2', 2, 1, subrect=(0, 0, 134, 96))
alien2.fps = 5
alien2.topleft = 100, 0

def update():
  alien.animate()
  alien2.animate()

def draw():
  screen.clear()
  alien.draw()
  alien2.draw()
  
pgzrun.go()