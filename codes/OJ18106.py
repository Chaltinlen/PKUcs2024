def go_around(out, start, n, N):
	if n >= 1:
		for i in range((N-n)//2, (N+n)//2):
			out[(N-n)//2][i] = start
			start += 1
		for i in range((N-n)//2+1, (N+n)//2):
			out[i][(N+n)//2-1] = start
			start += 1
		for i in range((n+N)//2-2, (N-n)//2-1, -1):
			out[(N+n)//2-1][i] = start
			start += 1
		for i in range((n+N)//2-2, (N-n)//2, -1):
			out[i][(N-n)//2] = start
			start += 1
		go_around(out, start, n-2, N)
	else:
		for line in out:
			print(*line, sep = " ")
n = int(input())
out = [[0 for i in range(n)] for j in range(n)]
go_around(out, 1, n, n)
