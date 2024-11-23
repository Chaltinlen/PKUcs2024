from sys import stdin, stdout
get = stdin.read().split()
ans = get[1]
for string in get[2:]:
	for i in range(len(ans)):
		if ans[i] != string[i]:
			ans = string[:i]
			break
stdout.write(ans+"\n")