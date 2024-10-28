t = int(input())
for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	print(min(n*min(a)+sum(b), n*min(b)+sum(a)))