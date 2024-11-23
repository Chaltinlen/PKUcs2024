from collections import Counter
n = int(input())
cnt = dict(Counter(map(int, input().split())))
n = max(cnt.keys())
dp = [[0 for i in range(n+1)] for j in range(2)]
a = [0 for i in range(n+2)]
for k in cnt:
	a[k] = cnt[k]
dp[1][1] = a[1]
dp[0][2] = a[1]
dp[1][2] = a[2] * 2
for i in range(3, n+1):
	dp[0][i] = max(dp[1][i-1], dp[1][i-2])
	dp[1][i] = dp[0][i-1] + i*a[i]
print(max(dp[0][n], dp[1][n]))