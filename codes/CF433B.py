def main():
	n = int(input())
	stones = list(map(int, input().split()))
	sortedstones = sorted(stones)
	sum_of_stones = [0, stones[0]]
	sum_of_stones_append = sum_of_stones.append
	sum_of_sortedstones = [0, sortedstones[0]]
	sum_of_sortedstones_append = sum_of_sortedstones.append

	for i in range(2, n+1):
		sum_of_stones_append(sum_of_stones[i-1] + stones[i-1])
		sum_of_sortedstones_append(sum_of_sortedstones[i-1] + sortedstones[i-1])

	m = int(input())
	for i in range(m):
		t, L, R = map(int, input().split())
		if t == 1:
			print(sum_of_stones[R] - sum_of_stones[L-1])
		else:
			print(sum_of_sortedstones[R] - sum_of_sortedstones[L-1])



main()