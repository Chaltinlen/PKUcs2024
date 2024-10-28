def main():
	n = int(input())
	t = sorted(map(int, input().split()))
	presum = 0
	cnt = 0
	for i in range(n):
		if t[i] >= presum:
			cnt += 1
			presum += t[i]
	print(cnt)

if __name__ == '__main__':
	main()