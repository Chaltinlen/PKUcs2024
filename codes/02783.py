while True:
	N = int(input())
	if N == 0:
		exit()
	dictlist = [{} for i in range(N)]
	for i in range(N):
		dictlist[i]["distance"], dictlist[i]["cost"] = map(int, input().split())
	dictlist = sorted(dictlist, key = lambda d: (d["distance"], d["cost"]))
	costmin = dictlist[0]["cost"]
	cnt = 1
	for i in range(1, N):
		if dictlist[i]["cost"] < costmin:
			cnt += 1
			costmin = dictlist[i]["cost"]
	print(cnt)