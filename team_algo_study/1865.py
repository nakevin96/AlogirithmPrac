# N개의 지점이 존재, N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 존재

import sys
input = sys.stdin.readline

# TC [1: 5]
INF = 10000001
TC = int(input().readline())
for _ in range(TC):
    # N(지점의 갯수) [1:500], M(도로 수) [1: 2500], W(웜홀 수) [1: 200]
    N, M, W = map(int, stdin.readline().rstrip().split(' '))
    road_info = []
    for _ in range(M):
        S, E, T = map(int, stdin.readline().rstrip().split(' '))
        road_info.append((S, E, T))
        road_info.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, stdin.readline().rstrip().split(' '))
        road_info.append((S, E, -T))

    dist = [INF for _ in range(N + 1)]
    dist[1] = 0
    for n in range(N):
        is_changed = False
        for road in road_info:
            if dist[road[1]] > dist[road[0]] + road[2]:
                dist[road[1]] = dist[road[0]] + road[2]
                is_changed = True

        if n == N - 1:
            if is_changed:
                print("YES")
            else:
                print("NO")


