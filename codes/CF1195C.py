n = int(input())
h = [list(map(int, input().split())) for i in range(2)]
chosen = [[0 for i in range(n + 1)] for j in range(2)]
for i in range(1, 1 + n):
    chosen[0][i] = max(h[0][i - 1] + chosen[1][i - 1], chosen[0][i - 1])
    chosen[1][i] = max(h[1][i - 1] + chosen[0][i - 1], chosen[1][i - 1])
print(max(chosen[0][n], chosen[1][n]))