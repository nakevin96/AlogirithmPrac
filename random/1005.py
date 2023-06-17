# 서기 2012년 ACM 크래프트 발매
# 건물 짓는 순서가 없음.
# 매 게임 시작시 건물 짓는 순서 부여
# 모든 건물 건설 시작부터 완성까지 딜레이 존재

# 특정 건물을 지을 때까지 걸리는 최소 시간 구하기
import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    # N 건물 번호, K : 건설 순서 규칙 // 건물 번호는 1~N
    N, K = map(int, input().split(' '))

    build_cost_list = [0]
    build_cost_list.extend(list(map(int, input().split(' '))))

    next_move = [[] for _ in range(N + 1)]
    inner_count = [0 for _ in range(N+1)]
    inner_count[0] = -1

    for _ in range(K):
        x, y = map(int, input().split(' '))
        next_move[x].append(y)
        inner_count[y] += 1

    W = int(input())

    check_list = deque([i for i, count in enumerate(inner_count) if count == 0])
    one_way_list = []

    while check_list:
        curr_point = check_list.popleft()
        one_way_list.append(curr_point)

        for next_point in next_move[curr_point]:
            inner_count[next_point] -= 1
            if inner_count[next_point] == 0:
                check_list.append(next_point)

    visited = [0 for _ in range(N+1)]
    for curr_point in one_way_list:
        for next_point in next_move[curr_point]:
            if visited[next_point] < visited[curr_point] + build_cost_list[curr_point]:
                visited[next_point] = visited[curr_point] + build_cost_list[curr_point]
    print(visited[W] + build_cost_list[W])

