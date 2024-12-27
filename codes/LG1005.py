from math import pow
n, m = map(int, input().split())
ans = 0
for _ in range(n):
    num = list(map(int, input().split()))
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = max(dp[i - 1][j] + pow(2, num[n - i + j]), dp[i - 1][j - 1] + pow(2, num[n - i - j ]))
    print(dp)