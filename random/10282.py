# https://www.acmicpc.net/problem/10282
# 문제를 읽고 생각한 문제 유형 => direct graph에서의 dfs or bfs
# 조건을 읽으면서 bfs가 아닌 heap 사용으로 전환
from sys import stdin
import heapq

input = stdin.readline

# 테스트 케이스 수 [1:100]
T = int(input())

for t in range(T):
    # 컴퓨터 수 n [1:10_000], 의존성 수 d [1:100_000],해킹당한 컴퓨터 번호 c [1 : 컴퓨터 수]
    n, d, c = map(int, input().rstrip().split(' '))
    computer_info = [-1 for _ in range(n + 1)]
    dependency_info = [[] for _ in range(n + 1)]
    virus_queue = [(0, c)]
    computer_info[c] = 0

    # 의존성 수 d만큼 각 의존성을 나타내는 a, b, s가 주어짐 a, b [1 : 컴퓨터수], s [0 : 1_000]
    # 컴퓨터 a가 컴퓨터 b를 의존하며 컴퓨터 b가 감염되면 s초후 컴퓨터 a도 감염
    for _d in range(d):
        a, b, s = map(int, input().rstrip().split(' '))
        dependency_info[b].append((a, s))

    while virus_queue:
        curr_time, curr_com = heapq.heappop(virus_queue)

        if (computer_info[curr_com] != -1) and (computer_info[curr_com] < curr_time):
            continue

        for next_com, duration in dependency_info[curr_com]:
            if (computer_info[next_com] == -1) or (computer_info[next_com] > curr_time + duration):
                computer_info[next_com] = curr_time + duration
                heapq.heappush(virus_queue, (curr_time + duration, next_com))

    infected_num = 0
    max_infected_time = 0
    for com in computer_info:
        if com != -1:
            infected_num += 1
        if max_infected_time < com:
            max_infected_time = com
    print(f'{infected_num} {max_infected_time}')
