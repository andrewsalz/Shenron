T = int(input())
for x in range(1, T+1):
    N = input()
    b = N.count("B")
    l = N.count(".")
    if (l > 0 and b >= l) or (l >= b and b > 1):
        result = "Y"
    else:
        result = "N"
    print("Case #{}: {}".format(x, result))