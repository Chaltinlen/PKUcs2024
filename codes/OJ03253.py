while True:
	n, p, m = map(int, input().split())
	if n == 0:
		break
	p -= 1
	if p == n:
		p = 0
	friends = [True for i in range(n)]
	order = []
	append = order.append
	for i in range(n):
		cnt = m
		while cnt:
			cnt -= 1
			p = (p+1) % n
			if not friends[p]:
				cnt += 1
		friends[p] = False
		if p == 0:
			p = n
		append(p)
	print(*order, sep = ",")