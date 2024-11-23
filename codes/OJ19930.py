minstep = 1e9
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def dfs(treasure, x, y, steps):
	global minstep

	for dx, dy in DIRECTIONS:
		nx, ny = x+dx, y+dy
		if treasure[nx][ny] == 1:
			minstep = min(minstep, steps)
		elif treasure[nx][ny] == 0:
			treasure[x][y] = 2
			dfs(treasure, nx, ny, steps+1)
			treasure[x][y] = 0
def main():
	m, n = map(int, input().split())
	treasure = [[2 for i in range(n+2)]] + [[2] + list(map(int, input().split())) + [2] for i in range(m)] + [[2 for i in range(n+2)]]
	if treasure[1][1] == 1:
		print(0)
		exit()
	dfs(treasure, 1, 1, 1)
	if minstep == 1e9:
		print("NO")
	else:
		print(minstep)
if __name__ == '__main__':
	main()