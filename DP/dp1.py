# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


def dp_fib(n, dp):
    if dp[n] != -1:
        return dp[n]
    elif n == 0:
        dp[n] = 0
        return dp[n]
    elif n == 1 or n == 2:
        dp[n] = 1
        return dp[n]
    dp[n] = dp_fib(n - 1, dp) + dp_fib(n - 2, dp)

    return dp[n]


if __name__ == "__main__":
    n = 10
    dp = [-1 for i in range(n + 1)]
    fib = dp_fib(n, dp)
    print(dp)
    print(fib)
