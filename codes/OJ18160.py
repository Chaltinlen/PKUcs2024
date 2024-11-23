from sys import setrecursionlimit
cnt = 0
setrecursionlimit(1<<30)
def dfs(board, x, y):
    global cnt
    board[x][y] = "."
    for dx, dy in direct:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == "W":
            cnt += 1
            dfs(board, nx, ny)
for i in range(int(input())):
    N, M = map(int, input().split())
    board = [["." for i in range(M+2)]] + [["."] + list(input()) + ["."] for i in range(N)] + [["." for i in range(M+2)]]
    direct = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1))
    maxcnt = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if board[i][j] == "W":
                cnt += 1
                dfs(board, i, j)
            maxcnt = max(cnt, maxcnt)
            cnt = 0
    print(maxcnt)