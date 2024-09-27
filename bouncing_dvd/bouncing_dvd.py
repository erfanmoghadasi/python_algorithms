import sys
sys.path.insert(0,"../modules")
import stddraw, color;

delay_time = 15

rectangle_width = .04
rectangle_height = .04

stddraw.setXscale(-1.0, 1.0)
stddraw.setYscale(-1.0, 1.0)
stddraw.setCanvasSize(800, 800)

rx, ry = 0.0, 0.1
vx, vy = 0.015, 0.023

while True:
    if abs(rx + vx) + rectangle_width > 1 : vx = -vx
    if abs(ry + vy) + rectangle_height > 1 : vy = -vy

    rx += vx
    ry += vy

    stddraw.clear(stddraw.WHITE)
    stddraw.filledRectangle(rx, ry, rectangle_width, rectangle_height)
    stddraw.show(delay_time)