def main():
	n = int(input())
	dictlist = [{} for i in range(n)]
	for i in range(n):
		dictlist[i]["price"], dictlist[i]["value"] = map(int, input().split())
	dictlist = sorted(dictlist, key = lambda d: d["price"])
	for i in range(n - 1):
		if dictlist[i]["value"] > dictlist[i+1]["value"]:
			print("Happy Alex")
			exit()
	print("Poor Alex")

main()