N = int(input())
if N <= 1:
    print(0)
else:
    prime_list = [i for i in range(N + 1)]
    prime_list[0] = 0
    prime_list[1] = 0
    div_num = 2
    limit = int(N ** 1 / 2)
    while div_num <= limit + 1:
        if prime_list[div_num] > 0:
            for dn in range(div_num + div_num, N + 1, div_num):
                prime_list[dn] = 0
        div_num += 1
    # prime_list는 정렬된 소수 모음
    prime_list = [n for n in prime_list if prime_list[n] != 0]
    prime_len = len(prime_list)

    ep = 0
    curr_sum = prime_list[0]
    result = 0
    for sp in range(prime_len):
        while ep < prime_len and curr_sum < N:
            ep += 1
            if ep == prime_len:
                break
            curr_sum += prime_list[ep]
        if ep == prime_len:
            break
        if curr_sum == N:
            result += 1
        curr_sum -= prime_list[sp]
    print(result)
