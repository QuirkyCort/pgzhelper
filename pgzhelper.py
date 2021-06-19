import math
import pygame
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER, transform_anchor
from pgzero import game, loaders
import sys
import time

_fullscreen = False

def set_fullscreen():
  global _fullscreen
  mod = sys.modules['__main__']
  mod.screen.surface = pygame.display.set_mode((mod.WIDTH, mod.HEIGHT), pygame.FULLSCREEN)
  _fullscreen = True

def set_windowed():
  global _fullscreen
  mod = sys.modules['__main__']
  mod.screen.surface = pygame.display.set_mode((mod.WIDTH, mod.HEIGHT))
  _fullscreen = False

def toggle_fullscreen():
  if _fullscreen:
    set_windowed()
  else:
    set_fullscreen()

def hide_mouse():
  pygame.mouse.set_visible(False)

def show_mouse():
  pygame.mouse.set_visible(True)

def distance_to(from_x, from_y, to_x, to_y):
  dx = to_x - from_x
  dy = to_y - from_y
  return math.sqrt(dx**2 + dy**2)

def direction_to(from_x, from_y, to_x, to_y):
  dx = to_x - from_x
  dy = from_y - to_y

  angle = math.degrees(math.atan2(dy, dx))
  if angle > 0:
    return angle

  return 360 + angle

def get_move(direction, distance):
  angle = math.radians(direction)
  dx = distance * math.cos(angle)
  dy = -distance * math.sin(angle)
  return (dx, dy)

def move(x, y, direction, distance):
  dx, dy = get_move(direction, distance)
  return (x + dx, y + dy)

class Collide():
  @staticmethod
  def line_line(l1x1, l1y1, l1x2, l1y2, l2x1, l2y1, l2x2, l2y2):
    determinant = (l2y2-l2y1)*(l1x2-l1x1) - (l2x2-l2x1)*(l1y2-l1y1)

    # Simplify: Parallel lines are never considered to be intersecting
    if determinant == 0:
      return False

    uA = ((l2x2-l2x1)*(l1y1-l2y1) - (l2y2-l2y1)*(l1x1-l2x1)) / determinant
    uB = ((l1x2-l1x1)*(l1y1-l2y1) - (l1y2-l1y1)*(l1x1-l2x1)) / determinant

    if 0 <= uA <= 1 and 0 <= uB <= 1:
      return True

    return False

  @staticmethod
  def circle_point(x1, y1, radius, x2, y2):
    rSquare = radius ** 2
    dSquare = (x2 - x1)**2 + (y2 - y1)**2

    if dSquare < rSquare:
      return True

    return False

  @staticmethod
  def circle_points(x, y, radius, points):
      rSquare = radius ** 2

      i = 0
      for point in points:
        try:
          px = point[0]
          py = point[1]
        except KeyError:
          px = point.x
          py = point.y
        dSquare = (px - x)**2 + (py - y)**2

        if dSquare < rSquare:
          return i
        i += 1

      return -1

  @staticmethod
  def circle_line(cx, cy, radius, x1, y1, x2, y2):
    x1 -= cx
    y1 -= cy
    x2 -= cx
    y2 -= cy

    if x2 < x1:
      x_min, x_max = x2, x1
    else:
      x_min, x_max = x1, x2

    if y2 < y1:
      y_min, y_max = y2, y1
    else:
      y_min, y_max = y1, y2

    # Coefficients of circle
    c_r2 = radius ** 2

    # Simplify if dx == 0: Vertical line
    dx = x2 - x1
    if dx == 0:
      d = c_r2 - x1**2
      if d < 0:
        return False
      elif d == 0:
        i = 0
      else:
        i = math.sqrt(d)
      if y_min <= i <= y_max or y_min <= -i <= y_max:
        return True
      return False
    
    # Gradient of line
    l_m = (y2 - y1) / dx

    # Simplify if l_m == 0: Horizontal line
    if l_m == 0:
      d = c_r2 - y1**2
      if d < 0:
        return False
      elif d == 0:
        i = 0
      else:
        i = math.sqrt(d)
      if x_min <= i <= x_max or x_min <= -i <= x_max:
        return True
      return False

    # y intercept
    l_c = y1 - l_m * x1


    # Coefficients of quadratic
    a = 1 + l_m**2
    b = 2 * l_c * l_m
    c = l_c**2 - c_r2

    # Calculate discriminant and solve quadratic  
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
      return False

    if discriminant == 0:
      d_root = 0
    else:
      d_root = math.sqrt(discriminant)

    i1 = (-b + d_root) / (2 * a)
    i2 = (-b - d_root) / (2 * a)

    if x_min <= i1 <= x_max or x_min <= i2 <= x_max:
      return True

    return False

  @staticmethod
  def circle_circle(x1, y1, r1, x2, y2, r2):
    rSquare = (r1 + r2) ** 2
    dSquare = (x2 - x1)**2 + (y2 - y1)**2

    if dSquare < rSquare:
      return True

    return False

  @staticmethod
  def circle_rect(cx, cy, cr, rx, ry, rw, rh):
    h_w = rw / 2
    h_h = rh / 2
    rect_l = rx - h_w
    rect_t = ry - h_h

    if cx < rect_l:
      dx2 = (cx - rect_l) ** 2
    elif cx > (rect_l + rw):
      dx2 = (cx - rect_l - rw) ** 2
    else:
      dx2 = 0

    if cy < rect_t:
      dy2 = (cy - rect_t) ** 2
    elif cy > (rect_t + rh):
      dy2 = (cy - rect_t - rh) ** 2
    else:
      dy2 = 0

    dist2 = dx2 + dy2

    if dist2 < (cr ** 2):
      return True

    return False

  @staticmethod
  def rect_point(x, y, w, h, px, py):
    half_w = w / 2
    half_h = h / 2
    
    if (
      px < x - half_w
      or px > x + half_w
      or py < y - half_h
      or py > y + half_h
    ):
      return False

    return True

  @staticmethod
  def rect_line(x, y, w, h, lx1, ly1, lx2, ly2):
    if (
      Collide.rect_point(x, y, w, h, lx1, ly1)
      or Collide.rect_point(x, y, w, h, lx2, ly2)
    ):
      return True

    half_w = w / 2
    half_h = h / 2
    rect_lines = [
      [x - half_w, y - half_h, x - half_w, y + half_h],
      [x - half_w, y - half_h, x + half_w, y - half_h],
      [x + half_w, y + half_h, x - half_w, y + half_h],
      [x + half_w, y + half_h, x + half_w, y - half_h],
    ]
    for line in rect_lines:
      if Collide.line_line(lx1, ly1, lx2, ly2, line[0], line[1], line[2], line[3]):
        return True
    
    return False

  @staticmethod
  def rect_rect(x1, y1, w1, h1, x2, y2, w2, h2):
    h_w1 = w1 / 2
    h_h1 = h1 / 2
    h_w2 = w2 / 2
    h_h2 = h2 / 2

    if (
      x2 - h_w2 > x1 + h_w1
      or x2 + h_w2 < x1 - h_w1
      or y2 - h_h2 > y1 + h_h1
      or y2 + h_h2 < y1 - h_h1
    ):
      return False

    return True

  @staticmethod
  def obb_point(x, y, w, h, angle, px, py):
    r_angle = math.radians(angle)
    costheta = math.cos(r_angle)
    sintheta = math.sin(r_angle)
    half_width = w / 2
    half_height = h / 2

    tx = px - x
    ty = py - y
    rx = tx * costheta - ty * sintheta
    ry = ty * costheta + tx * sintheta

    if rx > -half_width and rx < half_width and ry > -half_height and ry < half_height:
      return True

    return False

  @staticmethod
  def obb_points(x, y, w, h, angle, points):
    r_angle = math.radians(angle)
    costheta = math.cos(r_angle)
    sintheta = math.sin(r_angle)
    half_width = w / 2
    half_height = h / 2

    i = 0
    for point in points:
      try:
        px = point[0]
        py = point[1]
      except KeyError:
        px = point.x
        py = point.y

      tx = px - x
      ty = py - y
      rx = tx * costheta - ty * sintheta
      ry = ty * costheta + tx * sintheta

      if rx > -half_width and rx < half_width and ry > -half_height and ry < half_height:
        return i
      i += 1

    return -1

class Actor(Actor):
  def __init__(self, image, pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs):
    self._flip_x = False
    self._flip_y = False
    self._scale = 1
    self._mask = None
    self._animate_counter = 0
    self.fps = 5
    self.direction = 0
    super().__init__(image, pos, anchor, **kwargs)

  def distance_to(self, actor):
    return distance_to(self.x, self.y, actor.x, actor.y)

  def distance_toXY(self, x, y):
    return distance_to(self.x, self.y, x, y)

  def direction_to(self, actor):
    return direction_to(self.x, self.y, actor.x, actor.y)

  def direction_toXY(self, x, y):
    return direction_to(self.x, self.y, x, y)

  def move_towards(self, actor, dist):
    direction = self.direction_to(actor)
    self.x, self.y = move(self.x, self.y, direction, dist)

  def move_towardsXY(self, x, y, dist):
    direction = self.direction_toXY(x, y)
    self.x, self.y = move(self.x, self.y, direction, dist)

  def point_towards(self, actor, y=None):
    self.angle = self.direction_to(actor)

  def point_towardsXY(self, x, y):
    self.angle = direction_to(self.x, self.y, x, y)

  def move_in_direction(self, dist):
    self.x, self.y = move(self.x, self.y, self.direction, dist)

  def move_forward(self, dist):
    self.x, self.y = move(self.x, self.y, self.angle, dist)

  def move_left(self, dist):
    self.x, self.y = move(self.x, self.y, self.angle + 90, dist)

  def move_right(self, dist):
    self.x, self.y = move(self.x, self.y, self.angle - 90, dist)

  def move_back(self, dist):
    self.x, self.y = move(self.x, self.y, self.angle, -dist)

  @property
  def images(self):
    return self._images

  @images.setter
  def images(self, images):
    self._images = images
    if len(self._images) != 0:
      self.image = self._images[0]

  def next_image(self):
    if self.image in self._images:
      current = self._images.index(self.image)
      if current == len(self._images) - 1:
        self.image = self._images[0]
      else:
        self.image = self._images[current + 1]
    else:
      self.image = self._images[0]

  def animate(self):
    now = int(time.time() * self.fps)
    if now != self._animate_counter:
      self._animate_counter = now
      self.next_image()

  @property
  def angle(self):
    return self._angle

  @angle.setter
  def angle(self, angle):
    self._angle = angle
    self._transform_surf()

  @property
  def scale(self):
    return self._scale

  @scale.setter
  def scale(self, scale):
    self._scale = scale
    self._transform_surf()

  @property
  def flip_x(self):
    return self._flip_x

  @flip_x.setter
  def flip_x(self, flip_x):
    self._flip_x = flip_x
    self._transform_surf()

  @property
  def flip_y(self):
    return self._flip_y

  @flip_y.setter
  def flip_y(self, flip_y):
    self._flip_y = flip_y
    self._transform_surf()

  @property
  def image(self):
    return self._image_name

  @image.setter
  def image(self, image):
    self._image_name = image
    self._orig_surf = self._surf = loaders.images.load(image)
    self._update_pos()
    self._transform_surf()

  def _transform_surf(self):
    self._surf = self._orig_surf
    p = self.pos

    if self._scale != 1:
      size = self._orig_surf.get_size()
      self._surf = pygame.transform.scale(self._surf, (int(size[0] * self.scale), int(size[1] * self.scale)))
    if self._flip_x:
      self._surf = pygame.transform.flip(self._surf, True, False)
    if self._flip_y:
      self._surf = pygame.transform.flip(self._surf, False, True)

    self._surf = pygame.transform.rotate(self._surf, self._angle)

    self.width, self.height = self._surf.get_size()
    w, h = self._orig_surf.get_size()
    ax, ay = self._untransformed_anchor
    anchor = transform_anchor(ax, ay, w, h, self._angle)
    self._anchor = (anchor[0] * self.scale, anchor[1] * self.scale)

    self.pos = p
    self._mask = None

  def collidepoint_pixel(self, x, y=0):
    if isinstance(x, tuple):
      y = x[1]
      x = x[0]
    if self._mask == None:
      self._mask = pygame.mask.from_surface(self._surf)

    xoffset = int(x - self.left)
    yoffset = int(y - self.top)
    if xoffset < 0 or yoffset < 0:
      return 0

    width, height = self._mask.get_size()
    if xoffset > width or yoffset > height:
      return 0

    return self._mask.get_at((xoffset, yoffset))

  def collide_pixel(self, actor):
    for a in [self, actor]:
      if a._mask == None:
        a._mask = pygame.mask.from_surface(a._surf)

    xoffset = int(actor.left - self.left)
    yoffset = int(actor.top - self.top)

    return self._mask.overlap(actor._mask, (xoffset, yoffset))

  def collidelist_pixel(self, actors):
    for i in range(len(actors)):
      if self.collide_pixel(actors[i]):
        return i
    return -1

  def collidelistall_pixel(self, actors):
    collided = []
    for i in range(len(actors)):
      if self.collide_pixel(actors[i]):
        collided.append(i)
    return collided

  def obb_collidepoint(self, x, y):
    w, h = self._orig_surf.get_size()
    return Collide.obb_point(self.x, self.y, w, h, self._angle, x, y)

  def obb_collidepoints(self, points):
    w, h = self._orig_surf.get_size()
    return Collide.obb_points(self.x, self.y, w, h, self._angle, points)

  @property
  def radius(self):
    return self._radius

  @radius.setter
  def radius(self, radius):
    self._radius = radius

  def circle_collidepoints(self, points):
    return Collide.circle_points(self.x, self.y, self._radius, points)

  def circle_collidepoint(self, x, y):
    return Collide.circle_point(self.x, self.y, self._radius, x, y)

  def circle_collidecircle(self, actor):
    return Collide.circle_circle(self.x, self.y, self._radius, actor.x, actor.y, actor._radius)

  def circle_colliderect(self, actor):
    return Collide.circle_rect(self.x, self.y, self._radius, actor.left, actor.top, actor.width, actor.height)

  def draw(self):
    game.screen.blit(self._surf, self.topleft)

  def get_rect(self):
    return self._rect