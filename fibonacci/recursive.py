

def fibonacci(n, memo):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        if memo[n] == 0:
            memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]
    

def main():
    n = int(input("Enter the number of terms: "))
    memo = [0] * (n + 1)
    print(fibonacci(n, memo))

if __name__ == "__main__":
    main()