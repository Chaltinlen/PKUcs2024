from bisect import bisect
n = int(input())
x = list(sorted(map(int, input().split())))
q = int(input())
for i in range(q):
	print(bisect(x, int(input())))
	