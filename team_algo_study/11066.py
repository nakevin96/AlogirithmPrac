from sys import stdin

input = stdin.readline

for _ in range(int(input())):
    page_num = int(input())
    page_size_list = [0] + list(map(int, input().split(' ')))

    acc_sum = [0]
    for p_idx in range(1, page_num + 1):
        acc_sum.append(acc_sum[-1] + page_size_list[p_idx])

    dp = [[0 for _ in range(page_num + 1)] for _ in range(page_num + 1)]

    for check_len in range(1, page_num):
        for start in range(1, page_num):
            end = start + check_len
            if end > page_num:
                continue

            base = acc_sum[end] - acc_sum[start - 1]
            min_adder = float('inf')
            for divide_point in range(start, end):
                if dp[start][divide_point] + dp[divide_point + 1][end] < min_adder:
                    min_adder = dp[start][divide_point] + dp[divide_point + 1][end]
            dp[start][end] = base + min_adder
    print(dp[1][page_num])