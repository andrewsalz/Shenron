T = int(input())
for x in range(T):
    N = int(input())
    C = input()
    a = C.count("A")
    b = C.count("B")
    combo = N // 2
    if a == combo or b == combo:
        print("Case #{}: Y".format(x+1)
    else:
        print("Case #{}: N".format(x+1)