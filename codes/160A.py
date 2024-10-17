n = int(input())
coins = sorted(list(map(int, input().split())), reverse = True)
value = sum(coins)/2
taked = 0
for i in range(n):
	taked += coins[i]
	if taked > value:
		print(i+1)
		break
