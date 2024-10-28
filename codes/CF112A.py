s = list(input().lower())
t = list(input().lower())
for i in range(len(s)):
	if s[i] > t[i]:
		print(1)
		exit()
	if s[i] < t[i]:
		print(-1)
		exit()

print(0)

