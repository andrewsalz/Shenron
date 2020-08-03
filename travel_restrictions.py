T = int(input())
for x in range(1, T+1):
    N = int(input())
    inward = input()
    outward = input()
    print("Case #{}: ".format(x))
    for i in range(N):
        list_res = [N] * N
        list_res[i] = "Y"
        if outward[i] == "Y":
            y = i + 1
            while y < N and outward[y-1] == "Y":
                if inward[y] == "Y":
                    list_res[y] = "Y"
                    y += 1
                else:
                    break
            y = i - 1
            while y > -1 and outward[y+1] == "Y":
                if inward[y] == "Y":
                    list_res[y] = "Y"
                    y -= 1
                else:
                    break
        result = "".join(list_res)
        print(result)