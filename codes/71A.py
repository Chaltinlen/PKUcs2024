n = int(input())
for i in range(n):
	word = list(input())
	if len(word) <= 10:
		print(''.join(word))
	else:
		print(f"{word[0]}{len(word)-2}{word[-1]}")
