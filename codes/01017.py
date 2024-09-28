# 我就是那个只会用if else的不大聪明的
from math import ceil
while True:
	a = list(map(int, input().split()))
	if a == [0, 0, 0, 0, 0, 0]:
		break

	s = a[5]

	if a[4] > 0:
		s += a[4]
		a[0] = max(0, a[0] - 11 * a[4])

	if a[3] > 0:
		s += a[3]
		a[1] = a[1] - 5 * a[3]
		if a[1] < 0 and a[0] != 0:
			a[0] = max(0, a[0]+4*a[1])
			a[1] = 0

	if a[2] > 0:
		s += ceil(a[2] / 4)
		a[2] %= 4
		if a[2] != 0 and (not (a[1] == 0 and a[0] == 0)):
			a[1] -= 7 - 2* a[2]
			a[0] -= (8 - a[2] - 4*min(a[1], 0))

	if a[1] > 0:
		s += ceil(a[1] / 9)
		a[1] %= 9
		if a[1] != 0:
			a[0] -= (36 - 4*a[1])

	if a[0] > 0:
		s += ceil(a[0]/36)

	print(s)