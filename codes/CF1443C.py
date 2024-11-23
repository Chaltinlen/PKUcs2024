for i in range(int(input())):
	n = int(input())
	a = map(int, input().split())
	b = map(int, input().split())
	table = sorted(zip(a, b), reverse = True)
	tot = 0
	for j in range(n):
		if tot + table[j][1] < table[j][0]:
			tot += table[j][1]
		else:
			print(max(tot, table[j][0]))
			break
	else:
		print(tot)