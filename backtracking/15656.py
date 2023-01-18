n, m = map(int, input().split(" "))
n_list = sorted(map(int, input().split(" ")))


def sol(count):
    sol_result = []
    if count == 0:
        return [[]]
    for idx in range(n):
        item = n_list[idx]
        for tmp_result in sol(count - 1):
            sol_result.append([item, *tmp_result])
    return sol_result


result = sol(m)
for r in result:
    print(" ".join(map(str, r)))
