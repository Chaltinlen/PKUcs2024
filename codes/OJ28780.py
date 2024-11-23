def main():
    n, m = map(int, input().split())
    coins = set(map(int, input().split()))
    minimum = [0 if i not in coins else 1 for i in range(m+1)]
    for i in coins:
        for j in range(1+i, m+1):
            if minimum[j-i] == 0:
                continue
            else:
                if minimum[j] == 0:
                    minimum[j] = minimum[j-i] + 1
                else:
                    minimum[j] = min(minimum[j], minimum[j-i]+1)
    if minimum[-1] == 0:
        print(-1)
    else:
        print(minimum[-1])
main()