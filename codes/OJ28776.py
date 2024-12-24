n = int(input())
a, b = map(int, input().split())
hands = sorted([list(map(int, input().split())) for i in range(n)], key=lambda t: t[1] * t[0])
min_max_awa = 0
for i in range(1, n):
    a *= hands[i - 1][0]
    min_max_awa = max(min_max_awa, a // hands[i][1])
print(min_max_awa)
