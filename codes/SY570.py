n, q = map(int, input().split())
like = [[False for i in range(n)] for j in range(n)]
for i in range(q):
    x, y = map(int, input().split())
    like[x - 1][y - 1] = True
for i in range(n):
    for j in range(n):
        if like[i][j]:
            for k in range(n):
                if like[j][k] and like[k][i]:
                    print("Yes")
                    exit()
print("No")
