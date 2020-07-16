T = int(input())

for x in range(1, T+1):
    S = input()
    h_val = 0
    new_str = ""
    for j in range(len(S)):
        val = int(S[j])

        if h_val > val:
            new_str += ")" * (h_val - val)
        elif h_val < val:
            new_str += "(" * (val - h_val)
        new_str += S[j]
        
        h_val = val
    new_str += ")" * h_val

    print("Case #{}: {}".format(x, new_str))