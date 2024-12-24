from heapq import heappush, heappop
n = int(input())
a = list(map(int, input().split()))
health = 0
neg_cnt = []
pot_cnt = 0
for i in range(n):
    pot_cnt += 1
    health += a[i]
    if a[i] < 0:
        heappush(neg_cnt, a[i])
    while health < 0:
        health -= heappop(neg_cnt)
        pot_cnt -= 1
print(pot_cnt)
