# 녹색 옷 입은 애가 젤다지? : https://www.acmicpc.net/problem/4485
import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    heap = []
    heapq.heappush(heap, (map_info[start][start], start, start))
    distance[start][start] = map_info[start][start]

    while heap:
        cost, r, c = heapq.heappop(heap)

        if distance[r][c] < cost:
            continue

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc

            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue

            next_cost = cost + map_info[nr][nc]
            if next_cost < distance[nr][nc]:
                distance[nr][nc] = next_cost
                heapq.heappush(heap, (next_cost, nr, nc))


problem_count = 1
while True:
    N = int(input())
    if N == 0:
        break

    map_info = [list(map(int, input().split())) for _ in range(N)]
    distance = [[float('inf')] * N for _ in range(N)]

    dijkstra(0)

    print(f'Problem {problem_count}: {distance[N-1][N-1]}')
    problem_count += 1
