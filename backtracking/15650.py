# recursive 한 풀이
# n, m = map(int, input().split(" "))
# num_list = [i for i in range(1, n + 1)]
#
#
# def sol(n_list, count):
#     result = []
#     if count == 0:
#         return [[]]
#     for i in range(len(n_list)):
#         item = n_list[i]
#         rest_list = n_list[i + 1:]
#         for c in sol(rest_list, count - 1):
#             result.append([item] + c)
#     return result
#
#
# result_list = sol(num_list, m)
#
# for r in result_list:
#     print(" ".join(map(str, r)))
n, m = map(int, input().split(" "))
n_list = [i for i in range(1, n + 1)]


def sol(num_list, count):
    sol_result = []
    if count == 0:
        return [[]]
    for num_idx in range(len(num_list)):
        item = num_list[num_idx]
        rest_list = num_list[num_idx + 1:]
        for c in sol(rest_list, count - 1):
            sol_result.append([item, *c])
    return sol_result


result = sol(n_list, m)
for r in result:
    print(" ".join(map(str, r)))
