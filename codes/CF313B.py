def main():
	s = input()
	lens = len(s)
	n = int(input())
	pair = [0 for _ in range(lens)]
	pair[0] = 0

	# 预处理
	for i in range(lens - 1):
		pair[i + 1] = pair[i] 
		if s[i] == s[i + 1]:
			pair[i + 1] += 1
		
	# pair[-1] = pair[-2]
	# print(pair)
	for _ in range(n):
		L, R = map(int, input().split())
		print(pair[R - 1] - pair[L - 1])

main()