# 신종 바이스러인 웜 바이러스는 네트워크를 통해 전파

# 한 컴퓨터가 감염되면 네트워크 상에서 연결되어 있는 모든 컴퓨터가 바이러스에 걸림
# => 이런 유형의 문제는 BFS 사용하면 됨

import sys
from collections import deque

input = sys.stdin.readline

# 컴퓨터 수 [1: 100] 번호는 1번부터 매겨짐
computer_num = int(input())

# conntect info : 양방향으로 연결
connected_num = int(input())
connected_info = [[] for _ in range(computer_num + 1)]
for _ in range(connected_num):
    com1, com2 = map(int, input().split(' '))
    connected_info[com1].append(com2)
    connected_info[com2].append(com1)

queue = deque([1])
visited = [False for _ in range(computer_num + 1)]
visited[1] = True
while queue:
    curr_com = queue.popleft()

    for next_com in connected_info[curr_com]:
        if not visited[next_com]:
            visited[next_com] = True
            queue.append(next_com)

print(visited)
print(len([com for com in range(1, computer_num + 1) if visited[com]])-1)
