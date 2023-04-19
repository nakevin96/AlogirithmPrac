from sys import stdin

input = stdin.readline

# anta로 시작 tica로 끝남 -> antic 5개 무조건 들어가야 함
# 즉 k가 5보다 작으면 0

N, K = map(int, input().rstrip().split(' '))
word_list = []
for _ in range(N):
    word_list.append(input().rstrip()[4:-4])

# a~z 까지 배웠는지 체크
alpha_check = [False for _ in range(26)]
for needed in ['a', 'n', 't', 'i', 'c']:
    alpha_check[ord(needed) - ord('a')] = True

result = 0


def dfs(k_count, alpha_idx):
    global result
    if k_count == K - 5:
        # 다 배운 상태
        tmp_result = 0
        for word in word_list:
            is_done = True
            for c in word:
                if not alpha_check[ord(c) - ord('a')]:
                    is_done = False
                    break
            if is_done:
                tmp_result += 1
        result = max(result, tmp_result)
        return
    # 아직 다 안배운 상태
    for idx in range(alpha_idx, 26):
        if not alpha_check[idx]:
            alpha_check[idx] = True
            dfs(k_count + 1, idx + 1)
            alpha_check[idx] = False


if K < 5:
    print(0)
else:
    dfs(0, 0)
    print(result)
