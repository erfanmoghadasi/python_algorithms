#This is a Mont-Carlo simulation

import sys;
import random;

n = int(input('Please insert the number of matrix values : '))
trial = int(input('How many time you want to repeat the test? : '))

dead_ends = 0

for t in range(trial):
    matrix = [[False] * n for i in range(n)]
    x, y = n // 2, n // 2;

    while 0 < x < n -1 and 0 < y < n -1:
        if matrix[x+1][y] and matrix[x-1][y] and matrix[x][y+1] and matrix[x][y-1]:
            dead_ends += 1
            break;

        matrix[x][y] = True

        random_dot = random.randint(1,4)
        match random_dot:
            case 1: # Left
                if not (x == 0 or x == n -1) and not matrix[x-1][y]: x -= 1
            case 2: # Up
                if not (y == 0 or y == n -1) and not matrix[x][y+1]: y += 1
            case 3: # Right
                if not (x == 0 or x == n -1) and not matrix[x+1][y]: x += 1
            case 4: # Down
                if not (y == 0 or y == n -1) and not matrix[x][y-1]: y -= 1
            
dead_ends_possibility = dead_ends / trial * 100
print("the possibilty of the dead ends is: %i%%" % dead_ends_possibility)
