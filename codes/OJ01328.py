from math import sqrt, pow
for _ in range(1, int(1e9)):
	n, d = map(int, input().split())
	cnt = 0
	nosol = False
	if n == 0:
		break
	island = [list(map(int, input().split())) for i in range(n)]
	input()

	xcord = []
	append = xcord.append
	for isl in island:
		if isl[1] > d:
			print(f"Case {_}: {-1}")
			nosol = True
			break
		dist = sqrt(pow(d, 2) - pow(isl[1], 2))
		append((isl[0]-dist, isl[0]+dist))
	if nosol:
		continue

	xcord = sorted(xcord, key = lambda t: t[1])
	rht = -1e9
	for isl in xcord:
		if isl[0] > rht:
			cnt += 1
			rht = isl[1]
	print(f"Case {_}: {cnt}")