def main():
	n, w = map(int, input().split())
	val = 0
	candy = []
	append = candy.append
	for i in range(n):
		value, weight = map(int, input().split())
		append({"value": value, "weight": weight})
	candy = sorted(candy, key = lambda d: d["value"]/d["weight"], reverse = True)
	for dic in candy:
		if w >= dic["weight"]:
			val += dic["value"]
			w -= dic["weight"]
		else:
			val += w * dic["value"]/dic["weight"]
			break
	print(f"{val:.1f}")

main()