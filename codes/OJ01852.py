def main():
	N = int(input())
	for i in range(N):
		antmax = []
		antmin = []
		L, n = map(int, input().split())
		ant0 = map(int, input().split())
		for a in ant0:
			if a > L / 2:
				antmax.append(a)
				antmin.append(L-a)
			else:
				antmin.append(a)
				antmax.append(L-a)
		print(max(antmin), max(antmax))

main()