T = int(input()) # testcases
x = 1

while T > 0:
    M = []
    N = int(input()) # matrix size
    for y in range(N):
        M.append(list(map(int, input().split())))

    k = 0
    for a in range(N):
        k += M[a][a]
    
    r = 0
    for i in range(N):
        for b in range(1,N+1):
            if M[i].count(b) > 1:
                r += 1
                break
    c = 0
    for j in range(N):
        t = []
        for q in range(N):
            t.append(M[q][j])
        for g in range(1,N+1):
            if t.count(g) > 1:
                c += 1
                break
    print(f"Case #{x}: {k} {r} {c}")
    x += 1
    T -= 1