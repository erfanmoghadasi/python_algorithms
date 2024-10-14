import sys
sys.path.insert(0,"../modules")

import stdarray
import stdio

def _flow(is_open, is_full, i , j):
    n = len(is_full)
    if i < 0 or i >= n or j < 0 or j >= n: return
    if not is_open[i][j]: return
    if is_full[i][j] : return
    is_full[i][j] = True
    _flow(is_open, is_full, i+1, j)
    _flow(is_open, is_full, i-1, j)
    _flow(is_open, is_full, i, j+1)
    _flow(is_open, is_full, i, j-1)

# verical percoaltion
def flow_v(is_open):
    n = len(is_open)
    is_full = stdarray.create2D(n, n, False)
    for j in range(n):
        is_full[0][j] = is_open[0][j]
    for i in range(1, n):
        for j in range(n):
            is_full[i][j] = is_open[i][j] and is_full[i-1][j]
    return is_full

def flow(is_open):
    n = len(is_open)
    is_full = stdarray.create2D(n, n, False)
    for j in range(n):
        _flow(is_open, is_full, 0, j)
    return is_full

def percolates(is_open):
    n = len(is_open)
    is_full = flow(is_open)
    for j in range(n):
        if is_full[-1][j]:
            return True
    return False

def main():
    is_open = stdarray.readBool2D()
    stdarray.write2D(is_open)
    stdio.writeln(percolates(is_open))

if __name__ == "__main__":
    main()