from bisect import bisect_right
n = int(input())
h = list(map(int, input().split()))
testing = [-1] * (n + 1)
for i in h:
    testing[bisect_right(testing, i) - 1] = i
print(testing[::-1].index(-1))
