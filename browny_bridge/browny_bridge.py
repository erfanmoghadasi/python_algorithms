import sys
sys.path.insert(0,"../modules")
import stddraw, math, stdrandom;
from numpy import random;

def curve(x0, y0, x1, y1, variance, scale):

    #stop if interval is too small
    if x1 - x0 < 0.01:
        stddraw.line(x0, y0, x1, y1)
        stddraw.show(10)
        return
    
    x = (x0 + x1) / 2.0
    y = (y0 + y1) / 2.0

    delta = stdrandom.gaussian(0, math.sqrt(variance))

    curve(x0, y0, x, y + delta, variance / scale, scale)
    curve(x, y + delta, x1, y1, variance / scale, scale)

def main():
    n = float(input("How many for scale ? "))
    scale = 2 ** (2.0 * n)
    stddraw.setPenRadius(0.001)
    stddraw.clear(stddraw.LIGHT_GRAY)
    curve(0.0,0.5,1.0,0.5,.01, scale)
    stddraw.show()

if __name__ == "__main__":
    main()