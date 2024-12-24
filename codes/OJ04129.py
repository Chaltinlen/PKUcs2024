from collections import deque
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def bfs(x1, y1):
    global R, C, K
    queue = deque()
    queue.append((0, (x1, y1)))
    visited = set()
    while queue:
        time, coor = queue.popleft()
        time += 1
        x, y = coor[0], coor[1]
        if (time % K, (x, y)) in visited:
            continue
        visited.add((time % K, (x, y)))
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] == "E":
                    return time
                if time % K and maze[nx][ny] == "#":
                    continue
                else:
                    queue.append((time, (nx, ny)))
    return 1e9


for i in range(int(input())):
    R, C, K = map(int, input().split())
    maze = [input() for i in range(R)]
    x1, y1 = 0, 0
    for i in range(R):
        if "S" in maze[i]:
            x1 = i
            y1 = maze[i].index("S")
            break
    t = bfs(x1, y1)
    print(t if t != 1e9 else "Oop!")
