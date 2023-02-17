N, M = map(int, input().split(" "))

n_list = list(map(int, input().split(" ")))


def sol(count):
    if count == 0:
        return [[]]
    result = []
    for i in range(N):
        item = n_list[i]
        for r in sol(count - 1):
            result.append((item, *r))
    return result


s_sol = sorted(list(set(sol(M))))
for s in s_sol:
    print(" ".join(map(str, s)))
