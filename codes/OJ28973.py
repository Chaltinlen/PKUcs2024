from collections import deque
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def bfs():
    queue = deque()
    queue.append((0, (0, 1), True))  # step, head, _ishorizon
    inq = set()
    inq.add(((0, 1), True))
    while queue:
        step, head, _ishorizon = queue.popleft()
        print(head, _ishorizon)
        step += 1
        x, y = head[0], head[1]
        if _ishorizon and x + 1 < n and (not maze[x + 1][y]) and (not maze[x + 1][y - 1]) and ((x + 1, y - 1), False) not in inq:
            queue.append((step, (x + 1, y - 1), False))
            inq.add(((x + 1, y - 1), False))
        if not _ishorizon and y + 1 < n and (not maze[x - 1][y + 1]) and (not maze[x][y + 1]) and ((x - 1, y + 1), True) not in inq:
            if x == n - 1 and y == n - 1:
                return step
            queue.append((step, (x - 1, y + 1), True))
            inq.add(((x - 1, y + 1), True))
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if nx == n - 1 and ny == n - 1 and _ishorizon:
                return step
            if 0 <= nx < n and 0 <= ny < n and (not maze[nx][ny]) and ((nx, ny), _ishorizon) not in inq:
                if (_ishorizon and ny - 1 >= 0 and (not maze[nx][ny - 1])) or ((not _ishorizon) and nx - 1 >= 0 and (not maze[nx - 1][ny])):
                    queue.append((step, (nx, ny), _ishorizon))
                    inq.add(((nx, ny), _ishorizon))
    return -1
n = int(input())
maze = [list(map(int, input().split())) for i in range(n)]
if maze[0][0] or maze[0][1] or maze[n - 1][n - 2] or maze[n - 1][n - 1]:
    print(-1)
    exit()
print(bfs())