while True:
	R, n = map(int, input().split())
	if R == -1:
		break
	m = sorted(list(map(int, input().split())))
	
	cnt = 0
	last = m[0]
	plt = -R-1
	haveplt = False

	for i in range(1, n):
		if haveplt:
			if m[i] - plt > R:
				last = m[i]
				haveplt = False
		else:
			if m[i] - last > R:
				cnt += 1
				haveplt = True
				plt = m[i-1]
				if m[i] - plt > R:
					last = m[i]
					haveplt = False
	if m[-1] - plt > R:
		cnt += 1
	print(cnt)