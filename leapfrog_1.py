T = int(input())
for x in range(1, T+1):
    N = input()
    lily = []
    for i in N:
        lily.append(i)
    b = lily.count("B")
    l = lily.count(".")
    if b < l or b == 0 or l == 0:
        result = "N"
    else:
        result = "Y" 
    print("Case #{}: {}".format(x, result))