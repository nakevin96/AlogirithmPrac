# 텀 프로젝트 : https://www.acmicpc.net/problem/9466

T = int(input())
for _ in range(T):
    n = int(input())
    n_list = list(map(lambda x: int(x) - 1, input().split(' ')))
    check = [0 for _ in range(n)]
    for i in range(n):
        if n_list[i] == i:
            check[i] = 1
    result = 0
    for i in range(n):
        if check[i] == 0:
            is_done = False
            passed = set()
            check[i] = 1
            passed.add(i)
            next_i = n_list[i]
            while check[next_i] == 0:
                check[next_i] = 1
                passed.add(next_i)
                next_i = n_list[next_i]
            if next_i == i:
                is_done = True
            if not is_done:
                cycle = set()
                if next_i in passed:
                    while next_i not in cycle:
                        cycle.add(next_i)
                        next_i = n_list[next_i]
                result += (len(passed) - len(cycle))
    print(result)
