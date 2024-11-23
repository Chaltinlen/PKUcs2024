from itertools import accumulate
from math import comb
n = int(input())
*a, = accumulate(map(int, input().split()))
if a[:4] == [1, 0, 1, 1]:
	print()
if a[-1] % 3 or n < 3:
	print(0)
elif a[-1]:
	ans1 = 0
	ans = 0
	for num in a:
		if a[-1] / 3 == num:
			ans1 += 1
		if a[-1] / 3 == num / 2:
			ans += ans1
	print(ans)
else:
	print(comb(a.count(0)-1, 2))