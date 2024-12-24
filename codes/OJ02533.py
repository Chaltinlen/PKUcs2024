from bisect import bisect_left
n = int(input())
a = list(map(int, input().split()))
dp = [0x3f3f3f3f for i in range(n + 1)]
for t in a:
    dp[bisect_left(dp, t)] = t
print(dp.index(0x3f3f3f3f))
