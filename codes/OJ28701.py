n, k = map(int, input().split())
chicken = sorted(map(int, input().split()))
for i in range(k):
    if sum(chicken) / (k - i) < chicken[-1]:
        chicken.pop()
    else:
        print(f"{sum(chicken) / (k - i):.3f}")
        break
