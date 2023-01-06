'''
적록 색약은 빨간색과 초록의 차이를 느끼지 못한다
NxN 그리드의 각 칸에 RGB중 하나를 색칠한 그림이 있을 때
같은 색으로 칠해진 구역을 하나의 구역이라고 하였을 때
적록 색약이 보는 구역과 아닌 사람이 보는 구역을 구해라
'''
from sys import stdin
from collections import deque

n = int(stdin.readline().rstrip())
draw_info = []
visited_normal = [[0 for _ in range(n)] for _ in range(n)]
visited_patient = [[0 for _ in range(n)] for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(n):
    draw_info.append(list(stdin.readline().rstrip()))

normal_result = 0
patient_result = 0

for r in range(n):
    for c in range(n):
        if visited_normal[r][c] == 0:
            normal_result += 1
            normal_queue = deque([(r, c, draw_info[r][c])])

            while normal_queue:
                curr_r, curr_c, color = normal_queue.popleft()
                if visited_normal[curr_r][curr_c] == 1:
                    continue
                visited_normal[curr_r][curr_c] = 1
                for i in range(4):
                    nr = curr_r + dr[i]
                    nc = curr_c + dc[i]
                    if nr < 0 or nc < 0 or nr >= n or nc >= n:
                        continue
                    if visited_normal[nr][nc] == 0 and draw_info[nr][nc] == color:
                        normal_queue.append((nr, nc, color))

        if visited_patient[r][c] == 0:
            patient_result += 1
            if draw_info[r][c] == "G":
                patient_queue = deque([(r, c, "R")])
            else:
                patient_queue = deque([(r, c, draw_info[r][c])])
            while patient_queue:
                curr_r, curr_c, color = patient_queue.popleft()
                if visited_patient[curr_r][curr_c] == 1:
                    continue
                visited_patient[curr_r][curr_c] = 1
                for i in range(4):
                    nr = curr_r + dr[i]
                    nc = curr_c + dc[i]
                    if nr < 0 or nc < 0 or nr >= n or nc >= n:
                        continue
                    if color == "R" or color == "G":
                        if visited_patient[nr][nc] == 0 and draw_info[nr][nc] == "R" or draw_info[nr][nc] == "G":
                            patient_queue.append((nr, nc, draw_info[nr][nc]))
                    else:
                        if visited_patient[nr][nc] == 0 and draw_info[nr][nc] == color:
                            patient_queue.append((nr, nc, color))

print(f"{normal_result} {patient_result}")
