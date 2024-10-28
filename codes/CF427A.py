input()
a = list(map(int, input().split()))
free = 0
untreated = 0
for event in a:
	if event > 0:
		free += min(10, event)
	else:
		if free == 0:
			untreated += 1
		else:
			free -= 1
print(untreated)