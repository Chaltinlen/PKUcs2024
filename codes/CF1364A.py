from sys import stdin, stdout
from itertools import accumulate
def main():
	get = stdin.read().split("\n")
	out = []
	append = out.append
	for i in range(1, 2*int(get[0])+1, 2):
		n, x = map(int, get[i].split())
		a = [0]
		a.extend(list(map(int, get[i+1].split())))
		rem = list(accumulate(a, func = lambda m, n: (m + n) % x))
		status = [False for i in range(n)]

		if rem.count(0) != n+1:
			if rem[n] != 0:
				append(str(n))
			else:
				temp = [0, 0]
				for i in range(1, n):
					if rem[i] != rem[n]:
						temp[0] = n - i
						break
				for j in range(n-1, 0, -1):
					if rem[j] != 0:
						temp[1] = j
						break
				append(str(max(temp)))
		else:
			append(str(-1))
	append("\n")
	stdout.write("\n".join(out))

main()