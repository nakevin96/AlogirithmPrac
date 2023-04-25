# 백준 4803: https://www.acmicpc.net/problem/4803
import sys
from collections import deque

input = sys.stdin.readline


# bfs 풀이
# # bfs를 돌며 visited한 노드를 방문해야 하면 사이클 존재하는 것.
# def bfs(start_node):
#     queue = deque([start_node])
#     is_cycle = False
#     while queue:
#         curr_node = queue.popleft()
#         if visited[curr_node]:
#             is_cycle = True
#         visited[curr_node] = True
#         for next_node in edge_info[curr_node]:
#             if not visited[next_node]:
#                 queue.append(next_node)
#
#     return is_cycle
#
#
# # 입력을 받으면서 case증가시키고, 만약 ,n m이 둘다 0이면 반복문 탈출하기
# case = 0
#
# while True:
#     case += 1
#     n, m = map(int, input().rstrip().split(' '))
#     if n == 0 and m == 0:
#         break
#
#     visited = [False for _ in range(n + 1)]
#     edge_info = [[] for _ in range(n + 1)]
#     for _ in range(m):
#         v1, v2 = map(int, input().rstrip().split(' '))
#         edge_info[v1].append(v2)
#         edge_info[v2].append(v1)
#     result = 0
#     for node in range(1, n + 1):
#         if not visited[node]:
#             if not bfs(node):
#                 result += 1
#     if result == 0:
#         print(f'Case {case}: No trees.')
#     elif result == 1:
#         print(f'Case {case}: There is one tree.')
#     else:
#         print(f'Case {case}: A forest of {result} trees.')

# dfs 풀이
def findCycle(start):
    for adj_node in graph[start]:
        # 인접 노드가 자신의 부모 노드인 경우 패스
        if parent[start] == adj_node:
            continue

        # 인접 노드가 부모 노드가 아닌데 방문 이력이
        # 있다는 것은 곧 사이클을 의미함
        if visited[adj_node]:
            return True

        parent[adj_node] = start
        visited[adj_node] = 1
        # 인접 노드를 루트 노드로 하는 서브트리에
        # 사이클이 존재하면 곧 전체 트리에 사이클이
        # 존재하는 것과 같음
        if findCycle(adj_node):
            return True

    return False


n, m = map(int, input().split())
case = 1

while n != 0 or m != 0:
    graph = [[] for _ in range(n + 1)]
    parent = [-1] * (n + 1)
    visited = [0] * (n + 1)
    count = 0

    # 양방향 매핑
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # visited가 0인 모든 노드를 돌면서
    # 가능한 모든 연결 요소(연결 그래프)를 순회함
    for node in range(1, n + 1):
        if visited[node] == 0:
            parent[node] = node
            visited[node] = 1
            if not findCycle(node):
                count += 1

    if count == 0:
        print(f'Case {case}: No trees.')
    elif count == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {count} trees.')

    case += 1
    n, m = map(int, input().split())
