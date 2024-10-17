# F = [1, 1]
# for i in range(2, 20):
# 	F.append(F[i-1] + F[i-2])
# print(F)
F = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
n = int(input())
for i in range(n):
	print(F[int(input()) - 1])