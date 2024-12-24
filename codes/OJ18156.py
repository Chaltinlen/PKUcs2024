T = int(input())
S = sorted(map(int, input().split()))
n = len(S)
min_diff = 1e9
is_pos = True
abs_min_diff = 1e9
for i in range(n):
    for j in range(n - 1, i, -1):
        diff = S[i] + S[j] - T
        abs_diff = abs(diff)
        if abs_diff < abs_min_diff:
            min_diff = diff
            abs_min_diff = abs_diff
            is_pos = True if diff > 0 else False
        elif abs_diff == abs_min_diff and is_pos and diff < 0:
            min_diff = -min_diff
            is_pos = False
        else:
            if diff < 0:
                break
    if min_diff == 0 or i > T + abs_min_diff:
        break
print(T + min_diff)
