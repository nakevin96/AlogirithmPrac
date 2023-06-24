# 산성 용액, 알칼리 용액
# 산성 1~ 1_000_000_000
# 알칼리성 -1 ~ -1_000_000_000

N = int(input())
solution_list = list(map(int, input().split(' ')))

p1, p2 = 0, N-1
result_val = [solution_list[p1], solution_list[p2]]
min_result = abs(solution_list[p1] + solution_list[p2])

while p1 < p2:
    tmp_val = solution_list[p1] + solution_list[p2]
    if abs(tmp_val) < min_result:
        min_result = abs(tmp_val)
        result_val = [solution_list[p1], solution_list[p2]]

    if tmp_val == 0:
        break
    elif tmp_val < 0:
        p1 += 1
    else:
        p2 -= 1
print(*result_val)
