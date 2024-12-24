val = list(map(int, input().split(",")))
n = len(val)
dp = [[0 for i in range(n + 1)] for j in range(2)]
dp[0][1] = val[0]
dp[0][2] = max(val[0] + val[1], val[1])
dp[1][2] = val[1]
for i in range(2, 1 + n):
    dp[0][i] = max(dp[0][i - 1] + val[i - 1], val[i - 1])
    dp[1][i] = max(dp[1][i - 1] + val[i - 1], dp[0][i - 2] + val[i - 1])
print(max(map(max, dp)))
