from collections import defaultdict
n, M = map(int, input().split())
a = [0] + list(map(int, input().split())) + [M]
seta = set(a)
lit = defaultdict(int)
tot = 0
for i in range(1, n+2, 2):
	lit[a[i-1]+1] = tot + 1
	lit[a[i]] = tot + a[i] - a[i-1]
	tot = lit[a[i]]
max_lit = tot
for i in a[1::2]:
	if i-1 not in seta:
		max_lit = max(max_lit, M - tot + 2*lit[i - 1] - i + 1)
	if i+1 not in seta and i != M:
		max_lit = max(max_lit, M - tot + 2*lit[i] - i - 1)
print(max_lit)