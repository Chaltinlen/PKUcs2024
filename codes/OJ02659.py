A, B, K = map(int, input().split())
status = [tuple(map(int, input().split())) for i in range(K)]
pos = {(i, j) for i in range(A) for j in range(B)}
for st in status:
	opset = {(i, j) for i in range(st[0]-st[2]//2-1, st[0]+st[2]//2) for j in range(st[1]-st[2]//2-1, st[1]+st[2]//2) if i>=0 and i<=A-1 and j>=0 and j<=B-1}
	if st[3]:
		pos &= opset
	else:
		pos -= opset
print(len(pos))