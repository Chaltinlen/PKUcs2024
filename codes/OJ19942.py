def times(m1, m2):
	res = 0
	for i in range(p):
		for j in range(q):
			res += m1[i][j] * m2[i][j]
	return res
m, n, p, q = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(m)]
core = [list(map(int, input().split())) for j in range(p)]
ans = [[0 for j in range(n+1-q)] for i in range(m+1-p)]
for i in range(m+1-p):
	for j in range(n+1-q):
		ans[i][j] = times([row[j:j+q+1] for row in matrix[i:i+p+1]], core)

for i in ans:
	print(*i, sep = " ")