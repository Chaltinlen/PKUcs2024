for i in range(int(input())):
	n = int(input())
	*s, = map(int, input().split())
	acc = 0
	for i in s:
		if i == 2048:
			print("YES")
			break
		elif i > 2048:
			continue
		else:
			acc += i
	else:
		if acc >= 2048:
			print("YES")
		else:
			print("NO")
		