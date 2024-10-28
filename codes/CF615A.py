n, m = list(map(int, input().split()))
bulbs = [False for i in range(m)]
temp = []
for i in range(n):
	temp = list(map(int, input().split()))[1:]
#	print(temp)
	for num in temp:
		bulbs[num - 1] = True

for b in bulbs:
	if not b:
		print("NO")
		exit()

print("YES")