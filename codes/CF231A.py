n = int(input())
problems = 0
for i in range(n):
	a, b, c = list(map(int, input().split()))
	if a + b + c > 1:
		problems += 1

print(problems)
