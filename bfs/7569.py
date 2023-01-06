'''
철수의 토마토 농장에서 토마토를 보관하는 큰 창고를 갖고 있다
격자 모양 상자에 하나씩 넣은 다음 수직으로 쌓아 보관한다
토마토의 인접은 위 아래 왼쪽 오른쪽 앞 뒤 여섯방향이다
토마토들이 며칠 지나면 전부 익을 지 계산해라
'''

from sys import stdin
from collections import deque


def solution():
    m, n, h = map(int, stdin.readline().rstrip().split(" "))
    dm = [1, -1, 0, 0, 0, 0]
    dn = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    tomato_info = []
    queue = deque()
    is_completed = True
    for _h in range(h):
        tmp_box = []
        for _n in range(n):
            tmp_box.append(list(map(int, stdin.readline().rstrip().split(" "))))
            for _m in range(m):
                if tmp_box[_n][_m] == 0:
                    is_completed = False
                elif tmp_box[_n][_m] == 1:
                    queue.append((_h, _n, _m, 1))
                    tmp_box[_n][_m] = 0
        tomato_info.append(tmp_box)
    if is_completed:
        return 0

    for _h in range(h):
        for _n in range(n):
            for _m in range(m):
                while queue:
                    curr_h, curr_n, curr_m, curr_val = queue.popleft()
                    if tomato_info[curr_h][curr_n][curr_m] != 0:
                        continue
                    tomato_info[curr_h][curr_n][curr_m] = curr_val
                    for i in range(6):
                        nh = curr_h + dh[i]
                        nn = curr_n + dn[i]
                        nm = curr_m + dm[i]
                        if nh < 0 or nn < 0 or nm < 0 or nh >= h or nn >= n or nm >= m:
                            continue
                        if tomato_info[nh][nn][nm] == 0:
                            queue.append((nh, nn, nm, curr_val + 1))
    result = 0
    for _h in range(h):
        for _n in range(n):
            for _m in range(m):
                if tomato_info[_h][_n][_m] == 0:
                    return -1
                result = max(result, tomato_info[_h][_n][_m])
    return result - 1


print(solution())
