d = int(input())
n = int(input())
trash = [list(map(int, input().split())) for i in range(n)]
matrix = [[0 for i in range(1025)] for j in range(1025)]
for t in trash:
	for i in range(t[0]-d, t[0]+d+1):
		if i >= 0 and i < 1025:
			for j in range(t[1]-d, t[1]+d+1):
				if j >= 0 and j < 1025:
					matrix[i][j] += t[2]
maxij = max(map(max, matrix))
cnt = 0
for i in matrix:
	cnt += i.count(maxij)
print(cnt, maxij)