# 문자열 압축하기 : https://www.acmicpc.net/problem/2135
input_string = input()
dp = [[-1 for _ in range(len(input_string))] for _ in range(len(input_string))]


def is_repeated(r_check_start, r_check_end, divided_len):
    if (r_check_end - r_check_start + 1) % divided_len != 0:
        return False
    for check_idx in range(r_check_start + divided_len, r_check_end + 1):
        if input_string[check_idx] != input_string[check_idx - divided_len]:
            return False
    return True


def get_min_string_len(start_idx, end_idx):
    if start_idx == end_idx:
        dp[start_idx][end_idx] = 1

    if dp[start_idx][end_idx] != -1:
        return dp[start_idx][end_idx]

    dp[start_idx][end_idx] = end_idx - start_idx + 1

    for point_idx in range(start_idx, end_idx):
        divided_len_sum = get_min_string_len(start_idx, point_idx)
        divided_len_sum += get_min_string_len(point_idx + 1, end_idx)
        dp[start_idx][end_idx] = min(dp[start_idx][end_idx], divided_len_sum)

    for repeated_word_len in range(1, (end_idx - start_idx + 1) + 1):
        if is_repeated(start_idx, end_idx, repeated_word_len):
            compressed_len = len(str((start_idx - end_idx + 1) // repeated_word_len))
            compressed_len += 2
            compressed_len += get_min_string_len(start_idx, start_idx + repeated_word_len - 1)
            dp[start_idx][end_idx] = min(dp[start_idx][end_idx], compressed_len)

    return dp[start_idx][end_idx]


print(get_min_string_len(0, len(input_string) - 1))
