'''
도화지에 그림이 그려져있다. 이 때 그림의 갯수와 그림 중 넓이가 가장 넓은 것의 값을 출력
1로 연결된 것을 한 그림이라고 정의

입력은 세로 길이 n과 가로길이 m이 주어짐
'''

from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().rstrip().split(" "))
drawing_map = []
for _ in range(n):
    drawing_map.append(list(map(int, stdin.readline().rstrip().split(" "))))

result1 = 0
result2 = 0
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]
for _n in range(n):
    for _m in range(m):
        if drawing_map[_n][_m] == 1:
            result1 += 1
            tmp_result2 = 0
            queue = deque([(_n, _m)])
            while queue:
                curr_n, curr_m = queue.popleft()
                if drawing_map[curr_n][curr_m] != 1:
                    continue
                tmp_result2 += 1
                drawing_map[curr_n][curr_m] = -1
                for i in range(4):
                    if curr_n + dn[i] < 0 or curr_n + dn[i] >= n or curr_m + dm[i] < 0 or curr_m + dm[i] >= m:
                        continue
                    if drawing_map[curr_n + dn[i]][curr_m + dm[i]] == 1:
                        queue.append((curr_n + dn[i], curr_m + dm[i]))
            result2 = max(result2, tmp_result2)
print(result1)
print(result2)
