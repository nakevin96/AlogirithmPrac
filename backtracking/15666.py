N, M = map(int, input().split(" "))

N_list = list(map(int, input().split(" ")))
N_list.sort()


def sol(s_list, count):
    if count == 0:
        return {()}
    result = set()
    for idx in range(len(s_list)):
        item = s_list[idx]
        for r in sol(s_list[idx:], count - 1):
            result.add((item, *r))
    return result


s_result = sol(N_list, M)
s_result = sorted(list(s_result))
for s in s_result:
    print(" ".join(map(str, s)))
