rose = input()
n = len(rose)
dp = [[0 for i in range(n)] for i in range(2)]
if rose[0] == "R":
    dp[1][0] = 1
    dp[0][0] = 0
else:
    dp[0][0] = 1
    dp[1][0] = 0
for i in range(1, n):
    if rose[i] == "B":
        dp[0][i] = dp[0][i - 1] + 1
        dp[1][i] = min(dp[0][i - 1] + 1, dp[1][i - 1])
    else:
        dp[1][i] = dp[1][i - 1] + 1
        dp[0][i] = min(dp[1][i - 1] + 1, dp[0][i - 1])
print(min(dp[0][i], dp[1][i] + 1))