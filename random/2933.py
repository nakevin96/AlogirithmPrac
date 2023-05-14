# 미네랄: https://www.acmicpc.net/problem/2933
import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().rstrip().split(' '))
map_info = []
for _ in range(R):
    map_info.append(list(input().rstrip()))

N = int(input())
height_list = list(map(lambda x: int(x) - 1, input().rstrip().split(' ')))

is_left = False


def find_block(is_direction_left, tmp_height):
    map_height = R - 1 - tmp_height
    find_block_result = False
    if is_direction_left:
        for check in range(C - 1):
            if map_info[map_height][check] == 'x':
                find_block_result = True
                map_info[map_height][check] = '.'
                break
    else:
        for check in range(C - 1, -1, -1):
            if map_info[map_height][check] == 'x':
                find_block_result = True
                map_info[map_height][check] = '.'
                break
    return find_block_result


for height in height_list:
    is_left = not is_left
    is_block_broken = find_block(is_left, height)
    if not is_block_broken:
        continue
    cluster_list = [[False for _ in range(C)] for _ in range(R)]

    for bottom in range(C):
        if map_info[R - 1][bottom] == 'x' and not cluster_list[R - 1][bottom]:
            queue = deque([(R - 1, bottom)])
            cluster_list[R - 1][bottom] = True
            while queue:
                curr_r, curr_c = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = curr_r + dr
                    nc = curr_c + dc
                    if nr < 0 or nc < 0 or nr >= R or nc >= C:
                        continue
                    if map_info[nr][nc] == 'x' and not cluster_list[nr][nc]:
                        cluster_list[nr][nc] = True
                        queue.append((nr, nc))
                        # 바닥에 붙어있는 클러스터는 모두 체크된 상태
