import sys, stdio, percolationio, percolation

def evaluate(n, p, trials):
    count = 0.0
    for t in range(trials):
        is_open = percolationio.random(n, p)
        if percolation.percolates(is_open):
            count += 1
    if count == 0:
        return 0.0
    return count / trials

def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    trials = int(sys.argv[3])
    q = evaluate(n, p, trials)
    stdio.writeln(q)

if __name__ == "__main__":
    main()