t = int(input())
for i in range(t):
	n, x = map(int, input().split())
	a = list(map(int, input().split()))
	status = [0 for i in range(n+1)]
	for i in range(n):
		status[i+1] = (status[i] + a[i]) % x

	if status.count(0) == n+1:
		print(-1)
	else:
		for m in range(n+1, 0, -1):
			for fwd in range(0, n-m+1):
				if status[fwd] != status[fwd + m]:
					print(m)
					break
			else:
				continue
			break