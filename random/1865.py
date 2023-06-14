# # 나라에 N개의 지점, 지점 사이 M개의 도로 W개의 웜홀 (도로는 양방향, 웜홀은 단방향)
# # 웜홀의 경우 도착하면 시간이 거꾸로 감 => 아마 heap써서 풀어야 할 듯
#
# # 한 지점에서 출발을 해 다시 원 위치로 돌아왔을 때, 시간이 되돌아가는 경우가 있는지 궁금함
# from sys import stdin
#
# input = stdin.readline
# INF = float('inf')
#
# # TC [1:5]
# TC = int(input())
#
# for _ in range(TC):
#     # N [1:500], M[1:2_500], W[1:200]
#     N, M, W = map(int, input().rstrip().split(" "))
#
#     # road_info = [[] for _ in range(N+1)]
#     dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
#     for n in range(N):
#         dist[n][n] = 0
#     for _m in range(M):
#         S, E, T = map(int, input().rstrip().split(" "))
#         # road_info[S].append([E, T])
#         # road_info[E].append([S, T])
#         dist[S][E] = min(dist[S][E], T)
#         dist[E][S] = min(dist[E][S], T)
#
#     # wormhole_info = [[] for _ in range(N+1)]
#     # for _w in range(W):
#     #    S, E, T = map(int,input().rstrip().split(" "))
#     #    wormhole_info[S].append([E, T])
#
#     # 웜홀과 도로를 조합하여 싸이클이 존재하고, 해당 싸이클의 코스트 합이 0보다 작으면 시간을 줄일 수 있겠다
#     # 혹은 각 지점 사이의 최단 거리를 구하기 위해 O(N^3)을 쓰고 그 후에도 값의 변화가 있다면 음수 간선 포함
#     # 이라고 판단하는 방식도 괜찮을 듯 2억회 내에 충분히 가능
#     for _w in range(W):
#         S, E, T = map(int, input().rstrip().split(" "))
#         # road_info[S].append([E, -T])
#         T *= -1
#         dist[S][E] = min(dist[S][E], T)
#
#     for mid in range(1, N + 1):
#         for start in range(1, N + 1):
#             for end in range(1, N + 1):
#                 dist[start][end] = min(dist[start][end], dist[start][mid] + dist[mid][end])
#
#     is_checked = False
#     for check in range(1, N + 1):
#         if dist[check][check] < 0:
#             print("YES")
#             is_checked = True
#             break
#     if not is_checked:
#         print("NO")
