# 계단 수 ex) 12321 , 45656 과 같이 인접한 모든 자리의 차이가 1인 경우
# N이 주어질 때 길이가 N이며 0~9까지 숫자가 모두 등장하는 계단 수가 몇개인지 구하기
import sys

input = sys.stdin.readline
MOD = 1000000000
MAX = (1 << 10)

N = int(input())
# dp[i][j] 는 마지막 자릿수가 i이고 0~9까지 어떤 숫자들을 썼는지 나타내는 비트 마스킹
dp = [[0 for _ in range(MAX)] for _ in range(10)]

for i in range(1, 10):
    dp[i][1 << i] = 1

for num_len in range(2, N + 1):
    tmp_dp = [[0 for _ in range(MAX)] for _ in range(10)]

    for last_num in range(10):
        for masking in range(MAX):
            if last_num > 0:
                tmp_dp[last_num - 1][masking | (1 << (last_num - 1))] += dp[last_num][masking]
                tmp_dp[last_num - 1][masking | (1 << (last_num - 1))] = tmp_dp[last_num - 1][
                                                                            masking | (1 << (last_num - 1))] % MOD
            if last_num < 9:
                tmp_dp[last_num + 1][masking | (1 << (last_num + 1))] += dp[last_num][masking]
                tmp_dp[last_num + 1][masking | (1 << (last_num + 1))] = tmp_dp[last_num + 1][
                                                                            masking | (1 << (last_num + 1))] % MOD

    dp = tmp_dp

print(sum(dp[i][MAX - 1] for i in range(10)) % MOD)