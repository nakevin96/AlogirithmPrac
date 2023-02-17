N, M = map(int, input().split(" "))

n_list = list(map(int, input().split(" ")))
n_list.sort()


def sol(c, s_list):
    if c == 0:
        return [[]]
    result = []
    for i in range(len(s_list)):
        item = s_list[i]
        rest = s_list[i:]
        for r in sol(c - 1, rest):
            result.append([item, *r])
    return result


sol_result = sol(M, n_list)
for s in sol_result:
    print(" ".join(map(str, s)))
