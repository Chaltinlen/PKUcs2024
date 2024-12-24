for i in range(int(input())):
    coins = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0}
    trans = {"even": 0, "up": 1, "down": -1}
    weight = {-1: "light", 1: "heavy"}
    tests = [input().split() for i in range(3)]
    for i in coins.keys():
        for j in (-1, 1):
            coins[i] = j
            for k in tests:
                if sum([coins[_] for _ in k[0]]) - sum([coins[_] for _ in k[1]]) != trans[k[2]]:
                    break
            else:
                print(f"{i} is the counterfeit coin and it is {weight[j]}.")
                break
        else:
            coins[i] = 0
            continue
        break
