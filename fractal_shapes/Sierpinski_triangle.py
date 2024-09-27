import sys
sys.path.insert(0,"../modules")
import stddraw, math, random, color;

n = int(input("How many dots ? "))

stddraw.setCanvasSize(720, 720)
stddraw.setPenRadius(0.001)
stddraw.setPenColor(color.DARK_GRAY)

cx = [0.0, 1.0, 0.5]
cy = [0.0, 0.0, math.sqrt(3)/2]
point_colors = [color.DARK_BLUE, color.DARK_GREEN, color.DARK_RED]

x, y = 0, 0

for i in range(n):
    random_index = random.randint(0,2)
    x = (x + cx[random_index]) / 2
    y = (y + cy[random_index]) / 2
    stddraw.setPenColor(point_colors[random_index])
    stddraw.point(x, y)
    stddraw.show(0)

stddraw.show()