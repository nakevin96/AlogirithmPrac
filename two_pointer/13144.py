N = int(input())
N_list = list(map(int, input().split(' ')))

if N == 1:
    print(1)
else:
    sp, ep = 0, 1
    num_set = {N_list[0]}
    result = 1
    while True:
        if ep < N:
            if N_list[ep] in num_set:
                num_set.remove(N_list[sp])
                sp += 1
            else:
                num_set.add(N_list[ep])
                ep += 1
                result += (ep - sp)
        if ep == N:
            break
    print(result)
