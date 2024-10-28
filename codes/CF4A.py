w = int(input())
if w < 3:
	print("NO")
	exit()
else:
	print(["YES", "NO"][w % 2])