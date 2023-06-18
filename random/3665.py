# ACM-ICPC n개의 팀 참여
# 팀 1~n까지 번호 부여

# 작년에 비해 상대적 순위가 바뀐 팀만 발표
# 즉 작년 순위는 존재

from sys import stdin
from collections import deque
input = stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())

    connect_list = [set() for _ in range(n + 1)]
    incount_info = [0 for _ in range(n + 1)]
    incount_info[0] = -1

    rank = list(map(int, input().split(' ')))
    for ri in range(len(rank) - 1):
        for nri in range(ri + 1, len(rank)):
            connect_list[rank[ri]].add(rank[nri])
            incount_info[rank[nri]] += 1

    m = int(input())
    for _ in range(m):
        team1, team2 = map(int, input().split(' '))

        if team1 in connect_list[team2]:
            connect_list[team2].remove(team1)
            incount_info[team1] -= 1
            connect_list[team1].add(team2)
            incount_info[team2] += 1
        else:
            connect_list[team1].remove(team2)
            incount_info[team2] -= 1
            connect_list[team2].add(team1)
            incount_info[team1] += 1

    queue = deque()

    for team in range(1, n+1):
        if incount_info[team] == 0:
            queue.append(team)

    if not queue:
        print("IMPOSSIBLE")
        continue

    flag = True
    answer = []
    while queue:
        if len(queue) > 1:
            flag = False
            break

        curr_team = queue.popleft()
        answer.append(curr_team)
        for next_team in connect_list[curr_team]:
            incount_info[next_team] -= 1
            if incount_info[next_team] == 0:
                queue.append(next_team)
            elif incount_info[next_team] < 0:
                flag = False
                break
    if not flag or len(answer) < n:
        print("IMPOSSIBLE")
    else:
        print(*answer)




