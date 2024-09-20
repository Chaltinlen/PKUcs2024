ja, ia = list(map(int, input().split()))  # j: 行数 i: 列数
A = [[0 for i in range(ia)] for j in range(ja)]
for j in range(ja):
	A[j] = list(map(int, input().split()))
# print(A)

jb, ib = list(map(int, input().split()))

if ia != jb:
	print("Error!")
	exit()

B = [[0 for i in range(ib)] for j in range(jb)]
for j in range(jb):
	B[j] = list(map(int, input().split()))

# print(B)

A_times_B = [[0 for i in range(ib)] for j in range(ja)]


for j in range(ja):
	for i in range(ib):
		ans = 0
		for ind in range(ia):
			# print(i, j)
			ans += A[j][ind] * B[ind][i]
			# print(ans)
		A_times_B[j][i] = ans

# print(A_times_B)

jc, ic = list(map(int, input().split()))
C = [[0 for i in range(ic)] for j in range(jc)]
if jc != ja or ic != ib:
	print("Error!")
	exit()

for j in range(jc):
	C[j] = list(map(int, input().split()))

for j in range(jc):
	for i in range(ic):
		print(C[j][i] + A_times_B[j][i], end = ' ')
	print()