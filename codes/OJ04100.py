def main():
	n = int(input())
	for i in range(n):
		k = int(input())
		sted = sorted([list(map(int, input().split())) for i in range(k)], key = lambda t: t[1])
		ed = 0
		cnt = 0
		for sta in sted:
			if sta[0] > ed:
				cnt += 1
				ed = max(sta[1], ed)
		print(cnt)


if __name__ == '__main__':
	main()