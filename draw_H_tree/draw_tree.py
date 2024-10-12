import sys
sys.path.insert(0,"../modules")
import stddraw;

def draw(n, d, x, y):
    if n == 0: 
        return
    
    x0, x1 = x - d/2, x + d/2
    y0, y1 = y - d/2, y + d/2

    stddraw.line(x0, y, x1, y)
    stddraw.line(x0, y0, x0, y1)
    stddraw.line(x1, y0, x1, y1)
    stddraw.show(10)
    
    draw(n-1, d/2, x0, y0)
    draw(n-1, d/2, x1, y0)
    draw(n-1, d/2, x0, y1)
    draw(n-1, d/2, x1, y1)
    
def main():
    n = int(input("How many levels ? "))
    stddraw.setPenRadius(0.001)
    draw(n, 0.5, 0.5, 0.5)
    stddraw.show()

if __name__ == "__main__":
    main()