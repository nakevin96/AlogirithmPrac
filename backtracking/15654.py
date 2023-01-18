n, m = map(int, input().split())

num_list = sorted(list(map(int, input().split(" "))))


def sol(n_list, count):
    sol_result = []
    if count == 0:
        return [[]]
    for idx in range(len(n_list)):
        item = n_list[idx]
        rest = [*n_list[:idx], *n_list[idx + 1:]]
        for tmp_result in sol(rest, count - 1):
            sol_result.append([item, *tmp_result])
    return sol_result


result = sol(num_list, m)
for r in result:
    print(" ".join(map(str, r)))
