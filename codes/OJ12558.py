n, m = map(int, input().split())
island = [[0 for i in range(m+2)]]
island.extend([[0]+list(map(int, input().split()))+[0] for i in range(n)])
island.append([0 for i in range(m+2)])
circ = 0
for i in range(1, 1+n):
	for j in range(1, 1+m):
		if island[i][j]:
			circ += [island[i][j+1], island[i][j-1], island[i+1][j], island[i-1][j]].count(0)
print(circ)