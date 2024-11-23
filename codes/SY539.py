from math import sqrt
def issquare(a):
	return (not a) or ((not bool(sqrt(int(a)) % 1)) and int(a))
def dfs(A):
	if issquare(A):
		return True
	for i in range(1, len(A)+1):
		if issquare(A[:i]) and dfs(A[i:]):
			return True
	return False
print("Yes" if dfs(input()) else "No")