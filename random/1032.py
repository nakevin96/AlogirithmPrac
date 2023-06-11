from sys import stdin
input = stdin.readline

N = int(input())

test_list = [input().rstrip() for _ in range(N)]
word_len = len(test_list[0])

result = []
for w_idx in range(word_len):
    is_match = True
    base = test_list[0][w_idx]
    for t_idx in range(N):
        if test_list[t_idx][w_idx] != base:
            is_match = False
            break
    if is_match:
        result.append(base)
    else:
        result.append('?')
print(''.join(result))
