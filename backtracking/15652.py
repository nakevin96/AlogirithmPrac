n, m = map(int, input().split(" "))
n_list = [i for i in range(1, n + 1)]


def sol(num_list, count):
    sol_result = []
    if count == 0:
        return [[]]
    for num_idx in range(len(num_list)):
        item = num_list[num_idx]
        rest_list = num_list[num_idx:]
        for c in sol(rest_list, count - 1):
            sol_result.append([item, *c])
    return sol_result


result = sol(n_list, m)
for r in result:
    print(" ".join(map(str, r)))
