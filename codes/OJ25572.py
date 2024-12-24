DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def dfs(x1, y1, x2, y2):
    maze[x1][y1] = 5
    for dx, dy in DIRECTIONS:
        nx1, nx2, ny1, ny2 = x1 + dx, x2 + dx, y1 + dy, y2 + dy
        if maze[nx1][ny1] != 1 and maze[nx2][ny2] != 1 and maze[nx1][ny1] != 5:
            if maze[nx1][ny1] == 9 or maze[nx2][ny2] == 9:
                print("yes")
                exit()
            else:
                dfs(nx1, ny1, nx2, ny2)
    maze[x1][y1] = 0
n = int(input())
maze = [[1] * (n + 2)] + [[1] + list(map(int, input().split())) + [1] for i in range(n)] + [[1] * (n + 2)]
x1, y1, x2, y2 = 0, 0, 0, 0
cnt = 0
for i in range(n + 2):
    if cnt != 2:
        while 5 in maze[i]:
            if cnt == 0:
                x1, y1 = i, maze[i].index(5)
                maze[x1][y1] = 1
                cnt += 1
            else:
                x2, y2 = i, maze[i].index(5)
                maze[x2][y2] = 0
                cnt += 1
                break
dfs(x1, y1, x2, y2)
print("no")
