n, m = map(int, input().split())
matrix = [[0 for i in range(m+2)]] + [[0] + list(map(int, input().split())) + [0] for i in range(n)] + [[0 for i in range(m+2)]]
newmatrix = [[0 for i in range(m)] for i in range(n)]
ind = [-1, 0, +1]
for i in range(1, n+1):
	for j in range(1, m+1):
		
		num = [matrix[i+p][j+q] for p in ind for q in ind if p != 0 or q != 0].count(1)
		if num < 2 or num >= 4:
			newmatrix[i-1][j-1] = 0
		elif num == 3:
			newmatrix[i-1][j-1] = 1
		else:
			newmatrix[i-1][j-1] = matrix[i][j]
for i in range(0, n):
	print(*newmatrix[i], sep = " ")