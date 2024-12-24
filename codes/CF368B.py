n, m = map(int, input().split())
a = list(map(int, input().split()))
nums = {a[n - 1]}
distinct = [1 for i in range(n)]
for i in range(n - 2, -1, -1):
    if a[i] not in nums:
        distinct[i] += distinct[i + 1]
        nums.add(a[i])
    else:
        distinct[i] = distinct[i + 1]
for i in range(m):
    print(distinct[int(input()) - 1])
