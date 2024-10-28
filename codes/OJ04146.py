# n = int(input())
# for n in range(0, 100):
# 	ans = 0
# 	for a1 in range(n, -1, -1):
# 		for a2 in range(n, -1, -1):
# 			for a3 in range(n, -1, -1):
# 				if a1 + a2 + a3 <= ans:
# 					continue
# 				if (not (a1 + a2 + a3) % 5) and (not (a2 + a3) % 3) and (not (a1 + a2) % 2):
# 					ans = a1+a2+a3

# 	print(n, ans, ans//5)

# 找到规律了?
n = int(input())
print(5*(9*(n//15) - 1 + [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9][n % 15]))