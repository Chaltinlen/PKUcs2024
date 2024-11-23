from sys import stdin, stdout
from math import log
n, K = map(int, stdin.read().split())
bit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
ans = []
for i in range(1 + int(log(n)/log(K))):
	ans.append(bit[n % K])
	n //= K
stdout.write("".join(reversed(ans)))