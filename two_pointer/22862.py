# 가장 긴 짝수 연속 부분 수열: https://www.acmicpc.net/problem/22862

N, K = map(int, input().split(' '))
N_list = list(map(int, input().split(' ')))

# 풀이 1
# ans, cnt = 0, 0
# if N_list[0] % 2 == 1:
#     cnt += 1
# en = 0
# for st in range(N):
#     while (en < N - 1) and (cnt + N_list[en + 1] % 2 <= K):
#         en += 1
#         cnt += N_list[en] % 2
#     ans = max(ans, en - st + 1 - cnt)
#     cnt -= N_list[st] % 2
# print(ans)

# 풀이 2
left, right = 0, 0
result = 0
tmp_result, count = 0, 0
if N_list[left] % 2 == 0:
    result += 1
    tmp_result += 1
else:
    count += 1
while right < N:
    while right < N and count <= K:
        right += 1
        if right == N:
            break
        if N_list[right] % 2 == 0:
            tmp_result += 1
            result = max(result, tmp_result)
        else:
            count += 1
    while count > K:
        if N_list[left] % 2 == 0:
            tmp_result -= 1
        else:
            count -= 1
        left += 1

print(result)
