N, M = map(int, input().split(" "))

n_list = list(map(int, input().split(" ")))


def sol(s_list, count):
    if count == 0:
        return [[]]
    result = []
    for i in range(len(s_list)):
        item = s_list[i]
        rest = [*s_list[:i], *s_list[i + 1:]]
        for r in sol(rest, count - 1):
            result.append((item, *r))
    return list(set(result))


s_result = sorted(sol(n_list, M))
for s in s_result:
    print(" ".join(map(str, s)))
