def main():
	n, L = map(int, input().split())
	a = sorted(list(set(map(int, input().split()))))
	maxdelta = 0
	for i in range(1, len(a)):
		if a[i] - a[i-1] > maxdelta:
			maxdelta = a[i] - a[i-1]
	maxdelta /= 2
	if a[0] != 0 and maxdelta < a[0]:
		maxdelta = a[0]
	if a[-1] != L and maxdelta < L - a[-1]:
		maxdelta = L - a[-1]

	print(maxdelta)

main()