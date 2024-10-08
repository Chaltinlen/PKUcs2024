while True:
	N = int(input())
	dictlist = [{} for i in range(N)]
	for i in range(N):
		dictlist[i]["cost"], dictlist[i]["distance"] = map(int, input().split())
	