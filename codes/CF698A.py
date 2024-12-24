n = int(input())
STATUS = ((False, False), (False, True), (True, False), (True, True))
a = [(True, True)] + [STATUS[i] for i in map(int, input().split())]
dp = [[0 for i in range(3)] for j in range(n + 1)]
for i in range(1, 1 + n):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + (0 if a[i][0] else 1)
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + (0 if a[i][1] else 1)
    dp[i][2] = min(dp[i - 1]) + 1
print(min(dp[n]))
