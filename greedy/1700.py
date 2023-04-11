from collections import defaultdict

N, K = map(int, input().split(' '))
K_list = list(map(int, input().split(' ')))
dic = defaultdict(list)
for i in range(K - 1, -1, -1):
    dic[K_list[i]].append(i)

if K <= N:
    print(0)
else:
    result = 0
    max_flag = K + 1
    check = [0 for _ in range(K + 5)]
    curr_set = set()
    curr_supply = 0
    while len(curr_set) < N:
        dic[K_list[curr_supply]].pop()
        check[K_list[curr_supply]] = max_flag if not dic[K_list[curr_supply]] else dic[K_list[curr_supply]][-1]
        curr_set.add(K_list[curr_supply])
        curr_supply += 1

    while curr_supply < K:
        dic[K_list[curr_supply]].pop()
        if K_list[curr_supply] in curr_set:
            check[K_list[curr_supply]] = max_flag if not dic[K_list[curr_supply]] else dic[K_list[curr_supply]][-1]
            curr_supply += 1
        else:
            # 현재 안꼽혀 있는 친구
            victim, victim_base = -1, -1
            #  교체 플러그 탐색
            for s in curr_set:
                if check[s] > victim_base:
                    victim = s
                    victim_base = check[s]
            # set에서 빼기
            curr_set.remove(victim)
            curr_set.add(K_list[curr_supply])

            result += 1
            check[K_list[curr_supply]] = max_flag if not dic[K_list[curr_supply]] else dic[K_list[curr_supply]][-1]
            curr_supply += 1
    print(result)
