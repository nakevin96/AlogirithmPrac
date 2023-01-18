n, m = map(int, input().split())
n_list = [i for i in range(1, n + 1)]


def sol(count):
    sol_result = []
    if count == 0:
        return [[]]
    for i in range(len(n_list)):
        item = n_list[i]
        for tmp_result in sol(count-1):
            sol_result.append([item, *tmp_result])
    return sol_result


result = sol(m)
for r in result:
    print(" ".join(map(str, r)))
