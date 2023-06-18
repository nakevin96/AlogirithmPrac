from sys import stdin
from collections import deque

input = stdin.readline

# N: 학생 수 (1 ~ N번 부여), M: 비교 수3
N, M = map(int, input().split(' '))

compare_list = [[] for _ in range(N + 1)]
prev_count = [0 for _ in range(N + 1)]
prev_count[0] = -1

for _ in range(M):
    s1, s2 = map(int, input().split(' '))
    compare_list[s1].append(s2)
    prev_count[s2] += 1

zero_list = deque([idx for idx, count in enumerate(prev_count) if count == 0])
result = []

while zero_list:
    curr_student = zero_list.popleft()
    result.append(str(curr_student))

    for next_student in compare_list[curr_student]:
        prev_count[next_student] -= 1
        if prev_count[next_student] == 0:
            zero_list.append(next_student)

print(' '.join(result))
