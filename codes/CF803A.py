n, k = map(int, input().split())
if k > n * n:
    print("-1")
    exit()
mat = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    if k == 0:
        break
    mat[i][i] = 1
    k -= 1
    for j in range(1, n - i):
        if k == 1:
            mat[i + 1][i + 1] = 1
            k -= 1
        if k == 0:
            break
        k -= 2
        mat[i][i + j] = 1
        mat[i + j][i] = 1
for i in range(n):
    print(*mat[i])
