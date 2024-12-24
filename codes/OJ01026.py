while(n := int(input())):
	a = list(map(lambda t: int(t) - 1, input().split()))
	an = 0
	T = []
	append = T.append
	for i in range(n):
		an = a[i]
		for j in range(int(1e9)):
			if an == i:
				append(j+1)
				break
			an = a[an]
	while((msg := input().split(" ", 1)) != ["0"]):
		k = int(msg[0])
		msg = list(msg[1].ljust(n, " "))
		origin = msg
		enc = [" " for i in range(n)]
		for i in range(n):
			t = i
			for j in range(k % T[i]):
				i = a[i]
			enc[i] = msg[t]
		print("".join(enc))
	print()