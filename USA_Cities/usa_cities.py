import stddraw, color;

# def input_to_float(input_message):
#     input_value = input(input_message)
#     return float(input_value)

# scale_message = "Pleas insert the %s scale point"
# x0 = input_to_float(scale_message % "x0")
# y0 = input_to_float(scale_message % "y0")
# x1 = input_to_float(scale_message % "x1")
# y1 = input_to_float(scale_message % "y1")

# The canvas scale points
x0 = 609905.0
y0 = 207205.0
x1 = 1304962.0
y1 = 600000.0

stddraw.setXscale(x0, x1)
stddraw.setYscale(y0, y1)
stddraw.setCanvasSize(1200, 720)
stddraw.setPenRadius(0.001)
stddraw.setPenColor(color.DARK_GRAY)
with open("./usa_cities.txt") as f:
    for p in f:
        text_list = p.strip().split(" ")
        points_list = list(filter(lambda x: x != "", text_list))
        point_x = float(points_list[0]),
        point_y = float(points_list[1]),
        stddraw.point(point_x[0], point_y[0])
        stddraw.show(0)

stddraw.show()