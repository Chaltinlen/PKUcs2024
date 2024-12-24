m = int(input())
n = int(input())
num = sorted(input().split(), key=lambda t: "" if not t else t * (40 // len(t)), reverse=True)
g_int = [[] for i in range(m + 1)]
for i in num:
    for j in range(m, len(i) - 1, -1):
        g_int[j] = max(g_int[j], g_int[j - len(i)] + [i], key=lambda t: -1 if not t else int("".join(t)))
print(int("".join(g_int[m])))
