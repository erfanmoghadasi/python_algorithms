# Let's asumme that in ninty percent of the cases, the page rank of a page is equal to the page rank of its links.
# And in ten percent of the cases, the page rank of a page is equal to the page rank of the page itself.

from . import stdio

n = stdio.readInt()
link_conuts = [[0] * n for i in range(n)]
out_degrees = [0] * n

while not stdio.isEmpty():
    i, j = stdio.readInt(), stdio.readInt()
    out_degrees[i] += 1
    link_conuts[i][j] += 1

for i in range(n):
    for j in range(n):
        p = 0.9 * (link_conuts[i][j] / out_degrees[i]) + (0.1 / n)

