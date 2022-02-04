# pgzhelper
Pygame Zero Helper was originally created to enhance Pygame Zero with additional capabilities that were available in Scratch (eg. move_forward, point_towards, distance_to), but it has since evolved to include a large number of collision detection functions that are useful in games.

The capabilities provided by pgzhelp can be roughly divided into...

* Actor enhancements
    * Additional capabilities for a Pygame Zero Actor
    * Examples: 
        * Movements: move_forward, point_towards
        * Animation: images, animate, fps
        * Image: scale, flip_x, flip_y
* Collision detection
    * Detect collision between points, lines, circles, rect (AABB), rect (OBB)
    * Examples:
        * Collide.circle_line() : Check if a circle is colliding with a line
        * Collide.obb_points() : Check if an OBB rect is colliding with any of the given points
* Utility
    * Small utility functions
    * Examples:
        * For Pygame Zero: toggle_fullscreen, hide_mouse
        * Movement and directions: distance_to, direction_to

## Wiki
Please see the wiki on github for more details.