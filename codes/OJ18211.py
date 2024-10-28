p = int(input())
a = sorted(list(map(int, input().split())))
fwd, bwd = 0, len(a) - 1
cnt = 0
sell = False
while True:
	while p >= a[fwd]:
		p -= a[fwd]
		cnt += 1
		sell = True
		fwd += 1
		if bwd < fwd:
			sell = False
			break
	if sell:
		cnt -= 1
		p += a[bwd]
		bwd -= 1
		sell = False
	else:
		break
print(cnt)

