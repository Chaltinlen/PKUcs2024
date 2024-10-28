def main():
	n = int(input())
	box = sorted(list(map(int, input().split())), reverse = True)
	status = [True for i in range(n)]
	cnt = 0
	for i in range(n):
		if status[i]:
			status[i] = False
			cnt += 1
			prev = box[i]
			for j in range(i, n):
				if box[j] < prev and status[j]:
					status[j] = False
					prev = box[j]

	print(cnt)

if __name__ == '__main__':
	main()