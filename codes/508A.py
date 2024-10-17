def main():
	n, m, k = map(int, input().split())
	status = [[False for i in range(m+2)] for j in range(n+2)]
	ind = [-1, +1]
	for i in range(k):
		row, col = map(int, input().split())
		if status[row][col] == False:
			status[row][col] = True
			for ind1 in ind:
				for ind2 in ind:
					if status[row+ind1][col+ind2] and status[row][col+ind2] and status[row+ind1][col]:
						print(i+1)
						exit()
	# ind = [-1, +1]
	# for i in range(k):
	# 	row, col = map(int, input().split())
	# 	row -= 1
	# 	col -= 1
	# 	if status[row][col] == False:
	# 		status[row][col] = True
	# 		for ind1 in ind:
	# 			for ind2 in ind:
	# 				try:
	# 					if status[row+ind1][col+ind2] and status[row][col+ind2] and status[row+ind1][col]:
	# 						print(i + 1)
	# 						exit()
	# 				except IndexError:
	# 					continue
	# 	else:
	# 		continue

	print(0)

main()

