from itertools import accumulate
for i in range(int(input())):
    num = set()
    n = int(input())
    a = [0] + list(accumulate(map(int, input().split())))
    cnt = 0
    for i in a:
        if i in num:
            num = {i}
            cnt += 1
        else:
            num.add(i)
    print(cnt)
