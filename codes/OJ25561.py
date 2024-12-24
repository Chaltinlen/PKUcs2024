def dfs(num_goods, pref, n):
    if num_goods == n:
        global min_price
        tot_tag = 0
        tot_off = 0
        for i in range(m):
            max_off = 0
            tagged = sum(pref[i])
            for j in coupon[i]:
                if tagged >= j:
                    max_off = max(max_off, coupon[i][j])
            tot_tag += tagged
            tot_off += max_off
        tot_off += tot_tag // 300 * 50
        min_price = min(min_price, tot_tag - tot_off)
    else:
        for i in goods[num_goods]:
            pref[i - 1].append(goods[num_goods][i])
            dfs(num_goods + 1, pref, n)
            pref[i - 1].pop()


n, m = map(int, input().split())
goods = [input().split() for i in range(n)]
coupon = [input().split() for i in range(m)]
for i in range(n):
    for j in range(len(goods[i])):
        goods[i][j] = map(int, goods[i][j].split(":"))
    goods[i] = dict(goods[i])
for i in range(m):
    for j in range(len(coupon[i])):
        coupon[i][j] = map(int, coupon[i][j].split("-"))
    coupon[i] = dict(coupon[i])

min_price = 1e9
dfs(0, [[] for i in range(m)], n)
print(min_price)
