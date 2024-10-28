M, L = map(int, input().split())
trees = [True for i in range(M + 1)]
for i in range(L):
	a, b = map(int, input().split())
	for ele in range(a, b + 1):
		trees[ele] = False
print(trees.count(True))
