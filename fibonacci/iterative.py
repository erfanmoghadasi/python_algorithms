def fibonacci(n: int) -> int:
    memo = [0] * (n + 1)
    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1):
        memo[i] = memo[i -1] + memo[i -2]
    return memo[n]



def main():
    n = int(input("Enter the number of terms: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()