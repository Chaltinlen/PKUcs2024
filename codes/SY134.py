perm_list = []
perm_set = set()
def perm(n, a, sta = [False] * 8, depth = 0, pref = ()):
    if depth == n and pref not in perm_set:
        perm_list.append(" ".join(map(str, pref)))
        perm_set.add(pref)
    for t in range(n):
        if sta[t]:
            continue
        sta[t] = True
        perm(n, a, sta, depth + 1, pref + tuple([a[t]]))
        sta[t] = False

n = int(input())
a = sorted(map(int, input().split()))
perm(n, a)
print(*perm_list, sep="\n")