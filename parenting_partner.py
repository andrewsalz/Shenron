T = int(input())

for x in range(1, T+1):
    N = int(input())
    start_end = []
    result = ""
    C_time = 0
    J_time = 0

    for j in range(N):
        S, E = map(int, input().split())
        start_end.append((S, E, j))
    start_end.sort()
    orig_pos = N*[None]
    for i in range(N):
        sched = start_end[i]
        if sched[0] >= C_time:
            C_time = sched[1]
            orig_pos[sched[2]] = "C"
        elif sched[0] >= J_time:
            J_time = sched[1]
            orig_pos[sched[2]] = "J"
        else:
            result = "IMPOSSIBLE"
            break
    if result != "IMPOSSIBLE":
        for y in orig_pos:
            result += y
        print("Case #{}: {}".format(x, result))
    else:
        print("Case #{}: {}".format(x, result))