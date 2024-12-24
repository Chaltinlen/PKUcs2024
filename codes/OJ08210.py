def check(dist):
    t, num = 0, 0
    for i in range(1, N + 2):
        if stone[i] - t < dist:
            num += 1
        else:
            t = stone[i]
    return num > M
L, N, M = map(int, input().split())
stone = [0] + [int(input()) for i in range(N)] + [L]
lo, hi = 0, L
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo - 1)
