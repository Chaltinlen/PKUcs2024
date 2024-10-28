n, m = map(int, input().split())
r = sorted(list(map(int, input().split())))
maxdiff = r[-1] - r[0]
diff = []
append = diff.append
for i in range(n-1):
	append(r[i+1] - r[i])
diff = sorted(diff, reverse = True)

for i in range(m-1):
	maxdiff -= diff[i]
print(maxdiff)