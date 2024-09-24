n = list(str(bin(int(input())))[2:])
for i in range(len(n)//2):
	if n[i] != n[-i-1]:
		print("No")
		exit()
print("Yes")
