from collections import deque
def main():
    N, D = map(int, input().split())
    stu = deque(int(input()) for i in range(N))
    
    ans = []
    while stu:
        premin = stu[0]
        premax = stu[0]
        free = []
        for i in range(len(stu)):
            h = stu.popleft()
            if h - premin <= D and premax - h <= D:
                free.append(h)
            else:
                stu.append(h)
            premax = max(premax, h)
            premin = min(premin, h)
        ans += sorted(free)
    print(*ans, sep = "\n")

   
    # TLE

    # sortedstu = sorted(stu)
    # for i in range(N):
    #     for j in range(N):
    #         if not stusta[j]:
    #             continue
    #         ind = stu[i:].index(sortedstu[j])+i
    #         swap = True
    #         for s in stu[i:ind]:
    #             if abs(s - sortedstu[j]) > D:
    #                 swap = False
    #                 break
    #         if swap:
    #             stusta[j] = False
    #             for k in range(ind, i, -1):
    #                 stu[k-1], stu[k] = stu[k], stu[k-1]
    #             break
    # for s in stu:
    #     print(s)
    

    # WA

    # last = 0
    # premax, premin = stu[0], stu[0]
    # stu.append(stu[N-1]+ D+1)
    # for i in range(1, N+1):
    #     premax = max(premax, stu[i])
    #     premin = min(premin, stu[i])
    #     if premax - stu[i] > D or stu[i] - premin > D:
    #         sortedstu = sorted(stu[last:i])
    #         for s in sortedstu:
    #             print(s)
    #         last = i
    #         premin = stu[i]
    #         premax = stu[i]
   

    # TLE

    # for i in range(N):
    #     premax = 0
    #     premin = int(1e9+1)
    #     ind = 0
    #     val = int(1e9+1)
    #     for j in range(N):
    #         if not stusta[j]:
    #             continue
    #         premax = max(premax, stu[j])
    #         premin = min(premin, stu[j])
    #         if stu[j] - premin <= D and premax - stu[j] <= D and stu[j] < val:
    #             ind = j
    #             val = stu[j]
    #     stusta[ind] = False
    #     print(val)


if __name__ == "__main__":
    main()
