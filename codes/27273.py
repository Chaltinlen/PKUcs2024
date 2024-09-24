import math
t = int(input())
for i in range(t):
	n = int(input())
	print(n*(n+1)//2-2 * (2**int(math.log2(n) + 1)-1))