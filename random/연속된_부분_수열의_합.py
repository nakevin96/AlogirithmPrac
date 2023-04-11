# https://school.programmers.co.kr/learn/courses/30/lessons/178870
def solution(sequence, k):
    en = 0
    curr_sum = 0
    result = []
    sub_len = 1000001
    for st in range(len(sequence)):
        while (en < len(sequence)) and curr_sum + sequence[en] <= k:
            curr_sum += sequence[en]
            if curr_sum == k and en - st + 1 < sub_len:
                sub_len = en - st + 1
                result = [st, en]
            en += 1

        if en == len(sequence):
            break
        curr_sum -= sequence[st]
    return result