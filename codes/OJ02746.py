def josephus(n, m):
	circ = [True for i in range(n)]
	last = 0
	for i in range(n - 1):
		cnt = 0
		while cnt < m:
			last = (last + 1) % n
			if circ[last]:
				cnt += 1
		circ[last] = False
	return circ.index(True)

def main():
	while True:
		n, m = map(int, input().split())
		if(m == 0):
			exit()
		ans = josephus(n, m)
		if ans == 0:
			print(n)
		else:
			print(ans)

main()
