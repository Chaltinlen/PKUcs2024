n = int(input())
stu = list(sorted(enumerate(map(int, input().split()), start = 1), key = lambda t: t[1]))
time = 0
for i in range(n):
	time += (stu[i][1] * (n-1-i))

print(*[t[0] for t in stu], sep = " ")
print(f"{time/n:.2f}")