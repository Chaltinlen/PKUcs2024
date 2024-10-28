def main():
	n = int(input())
	for i in range(n):
		s = int(input())
		a = int(input())
		A = sorted(list(map(int, input().split())))
		b = int(input())
		B = sorted(list(map(int, input().split())))
		cnt = 0
		ap, bp = 0, 0
		for ap in range(a):
			bp = 0
			while bp < b:
				if s - A[ap] > B[bp]:
					bp += 1
					continue
				elif s - A[ap] == B[bp]:
					bp += 1
					cnt += 1
					continue
				else:
					break
		print(cnt)

	
main()