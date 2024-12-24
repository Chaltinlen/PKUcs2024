while True:
    a, b = sorted(map(int, input().split()))
    if a == 0:
        break
    flag = True
    while b < 2 * a and b != a:
        flag = not flag
        a, b = b - a, a
    print("win" if flag else "lose")
