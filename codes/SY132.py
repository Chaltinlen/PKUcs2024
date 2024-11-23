def permutation(n, pres = []):
	if not n:
		print(*pres, sep = " ")
	else:
		for i in n:
			permutation([ntil for ntil in n if ntil != i], pres+[i])
def main():
	permutation(list(range(1, 1+int(input()))))
main()