import sys
sys.path.insert(0,"../modules")

import stdarray, stdrandom, stddraw, sys, percolation

def random(n, p):
    is_open = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            is_open[i][j] = True if stdrandom.bernoulli(p) else False
    return is_open

def draw(a, which):
    n = len(a)
    stddraw.setXscale(-.5, n)
    stddraw.setYscale(-.5, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n -1 -i, .45)

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])

    for t in range(trials):
        stddraw.clear()
        is_open = random(n, p)
        stddraw.setPenColor(stddraw.BLACK)
        draw(is_open, False)
        is_full = percolation.flow(is_open)
        stddraw.setPenColor(stddraw.BLUE)
        draw(is_full, True)
        stddraw.show(1000)

if __name__ == "__main__":
    main()


