DIRECTIONS = ((0, 0), (0, 1), (1, 0), (0, -1), (-1, 0))
def xor(change1, change2):
    return [[change1[i][j] ^ change2[i][j] for j in range(6)] for i in range(5)]
light = [list(map(int, input().split())) for i in range(5)]
ans = [[0 for i in range(6)] for j in range(5)]
change = [[[0,0,0,1,1,1],[1,0,1,0,1,0],[1,0,1,1,0,0],[0,0,1,0,0,0],[1,1,0,0,0,0]],[[1,0,1,0,1,0],[1,0,1,0,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0],[0,0,1,0,0,0]],[[1,0,1,1,0,0],[1,0,0,0,1,0],[0,1,1,0,1,1],[1,0,0,0,1,0],[1,0,1,1,0,0]],[[0,0,1,0,0,0],[0,1,1,1,0,0],[1,0,0,0,1,0],[1,0,1,0,1,1],[1,0,1,0,1,0]],[[1,1,0,0,0,0],[0,0,1,0,0,0],[1,0,1,1,0,0],[1,0,1,0,1,0],[0,0,0,1,1,1]]]
for j in range(4, -1, -1):
    for i in range(5):
        if light[i][j + 1]:
            ans[i][j] ^= 1
            for dx, dy in DIRECTIONS:
                nx, ny = i + dx, j + dy
                if 0 <= nx < 5 and 0 <= ny < 6:
                    light[nx][ny] ^= 1
for i in range(5):
    if light[i][0]:
        ans = xor(ans, change[i])
for i in range(5):
    print(*ans[i], sep=" ")