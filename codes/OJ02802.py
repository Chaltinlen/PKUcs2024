from heapq import heappop, heappush
DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def bfs(x1, y1, x2, y2):
    min_heap = []
    min_seg = 1e9
    min_heap.append((0, x1, y1, {(x1, y1)}, (0, 0)))
    while min_heap:
        seg, x, y, visited, last_dir = heappop(min_heap)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited:
                if (nx, ny) == (x2, y2):
                    min_seg = min(min_seg, seg + (1 if (dx, dy) != last_dir else 0))
                    break
                if board[ny][nx] == " ":
                    if seg + (1 if (dx, dy) != last_dir else 0) < min_seg:
                        heappush(min_heap, (seg + (1 if (dx, dy) != last_dir else 0), nx, ny, visited | {(nx, ny)}, (dx, dy)))
    return min_seg


for _ in range(1, int(1e9)):
    w, h = map(int, input().split())
    if w == 0:
        break
    print(f"Board #{_}:")
    board = [["X" for i in range(w + 4)]]\
     + [["X"] + [" " for i in range(w + 2)] + ["X"]]\
     + [["X", " "] + list(input()) + [" ", "X"] for i in range(h)]\
     + [["X"] + [" " for i in range(w + 2)] + ["X"]]\
     + [["X" for i in range(w + 4)]]
    for cnt in range(1, int(1e9)):
        x1, y1, x2, y2 = map(lambda t: int(t) + 1, input().split())
        if x1 == 1:
            break
        min_seg = bfs(x1, y1, x2, y2)
        if min_seg == 1e9:
            print(f"Pair {cnt}: impossible.")
        else:
            print(f"Pair {cnt}: {min_seg} segments.")
    print()