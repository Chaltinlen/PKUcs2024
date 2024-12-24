from heapq import heappop, heappush
m, n, p = map(int, input().split())
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def Dijkstra(x, y):
    global m, n
    visited = set()
    heap = [(0, (x, y))]
    dist = [[1e9 for i in range(n)] for j in range(m)]
    if mountain[x][y] == "#":
        return dist
    dist[x][y] = 0
    while heap:
        _, node = heappop(heap)
        x, y = node[0], node[1]
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and mountain[nx][ny] != "#":
                ndist = dist[x][y] + abs(int(mountain[nx][ny]) - int(mountain[x][y]))
                if dist[nx][ny] > ndist:
                    dist[nx][ny] = ndist
                    heappush(heap, (ndist, (nx, ny)))
    return dist


mountain = [input().split() for i in range(m)]
for i in range(p):
    prompt = list(map(int, input().split()))
    if mountain[prompt[2]][prompt[3]] == "#":
        print("NO")
    else:
        d = Dijkstra(prompt[0], prompt[1])[prompt[2]][prompt[3]]
        print(d if d != 1e9 else "NO")
