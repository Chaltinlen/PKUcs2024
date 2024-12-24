DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def snowboarding(x, y):
    max_slope = 0
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and zone[x][y] > zone[nx][ny]:
            if not dist[nx][ny]:
                snowboarding(nx, ny)
            max_slope = max(max_slope, dist[nx][ny])
    dist[x][y] = 1 + max_slope

R, C = map(int, input().split())
zone = [list(map(int, input().split())) for i in range(R)]
dist = [[0 for i in range(C)] for j in range(R)]
for i in range(R):
    for j in range(C):
        if not dist[i][j]:
            snowboarding(i, j)
print(max(map(max, dist)))