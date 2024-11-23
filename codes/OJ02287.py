while(n := int(input())):
    tian = sorted(map(int, input().split()))
    wang = sorted(map(int, input().split()))
    ans = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i] += (tian[(j + i) % n]-wang[j]) // abs(tian[(j + i) % n]-wang[j]) if tian[(j + i) % n] != wang[j] else 0
    print(200 * max(ans))