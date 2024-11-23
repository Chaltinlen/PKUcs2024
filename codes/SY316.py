def dfs(x, y, pref, weight, m, n):
	if x == n-1 and y == m-1:
		global maxw
		if weight > maxw:
			global path
			path = pref+[str(x+1)+" "+str(y+1)]
			maxw = weight
		return
	for dx, dy in DIRECTION:
		nx, ny = x+dx, y+dy
		if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
			visited[nx][ny] = True
			dfs(nx, ny, pref+[str(x+1)+" "+str(y+1)], weight + matrix[nx][ny], m, n)
			visited[nx][ny] = False
maxw = -1e9
DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
visited = [[False for i in range(m)] for j in range(n)]
visited[0][0] = True
path = []
matrix = [list(map(int, input().split())) for i in range(n)]
dfs(0, 0, [], matrix[0][0], m, n)
print(*path, sep = "\n")