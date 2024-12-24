from itertools import accumulate
t, k = map(int, input().split())
MOD = int(1e9 + 7)
m = int(1e5 + 1)
dp = [1 for i in range(m)]
for j in range(k, m):
    dp[j] = (dp[j - 1] + dp[j - k]) % MOD
dp = tuple(accumulate(dp, func=lambda x, y: (x + y) % MOD))
for i in range(t):
    a, b = map(int, input().split())
    print((dp[b] - dp[a - 1]) % MOD)
