from sys import stdin

input = stdin.readline

R, C = map(int, input().split(' '))
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
map_info = []
clear_info = [[True for _ in range(C)] for _ in range(R)]
curr_r, curr_c, curr_d = map(int, input().split(' '))

for _r in range(R):
    map_info.append(list(map(int, input().split(' '))))
    for _c in range(C):
        if map_info[_r][_c] == 0:
            clear_info[_r][_c] = False


def turn_left(curr_direction):
    if curr_direction == 0:
        return 3
    return curr_direction - 1


def can_move_forward(cr, cc, cd):
    nr, nc = cr + direction[cd][0], cc + direction[cd][1]
    if nr < 0 or nc < 0 or nr >= R or nc >= C:
        return False
    if map_info[nr][nc] == 0:
        return True
    return False


def can_move_backward(cr, cc, cd):
    back_direction = (cd + 2) % 4
    nr, nc = cr + direction[back_direction][0], cc + direction[back_direction][1]
    if nr < 0 or nc < 0 or nr >= R or nc >= C:
        return False
    if map_info[nr][nc] == 0:
        return True
    return False


def is_all_clear(cr, cc):
    clear_result = True
    for dr, dc in direction:
        nr, nc = cr + dr, cc + dc
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            continue
        if map_info[nr][nc] == 1:
            continue
        if not clear_info[nr][nc]:
            return False
    return True


result = 0
while True:
    if not clear_info[curr_r][curr_c]:
        result += 1
        clear_info[curr_r][curr_c] = True
    if is_all_clear(curr_r, curr_c):
        # 주변 청소 다 끝나고 후진이 불가능 한 경우 종료
        if not can_move_backward(curr_r, curr_c, curr_d):
            break
        # 청소가 다 끝나고 후진이 가능한 경우 : 한칸 후진
        else:
            back_d = (curr_d + 2) % 4
            curr_r, curr_c = curr_r + direction[back_d][0], curr_c + direction[back_d][1]
    else:
        is_find = False
        while True:
            if is_find:
                break
            # 반시계 회전
            curr_d = turn_left(curr_d)
            if can_move_forward(curr_r, curr_c, curr_d):
                next_r, next_c = curr_r + direction[curr_d][0], curr_c + direction[curr_d][1]
                if not clear_info[next_r][next_c]:
                    curr_r, curr_c = next_r, next_c
                    is_find = True
print(result)

# 클래스를 통한 풀이
# class Robot:
#     def __init__(self, start_r, start_c, start_direction):
#         self.r = start_r
#         self.c = start_c
#         self.d = start_direction
#         self.clean = 0
#         self.d_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#         self.db_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]
#
#     def move_front(self):
#         nr, nc = self.r + self.d_list[self.d][0], self.c + self.d_list[self.d][1]
#         if nr < 0 or nc < 0 or nr >= R or nc >= C:
#             return -1, -1
#         if room_info[nr][nc] == 0:
#             self.r, self.c = nr, nc
#             return self.r, self.c
#         return -1, -1
#
#     def move_back(self):
#         nr, nc = self.r + self.db_list[self.d][0], self.c + self.db_list[self.d][1]
#         if nr < 0 or nc < 0 or nr >= R or nc >= C:
#             return -1, -1
#         if room_info[nr][nc] != 1:
#             self.r, self.c = nr, nc
#             return self.r, self.c
#         return -1, -1
#
#     def rotate(self):
#         if self.d == 0:
#             self.d = 3
#         else:
#             self.d -= 1
#         nr, nc = self.r + self.d_list[self.d][0], self.c + self.d_list[self.d][1]
#         if (0 <= nr < R and 0 <= nc < C) and room_info[nr][nc] == 0:
#             return True
#         return False
#
#     def run(self):
#         while True:
#             if room_info[self.r][self.c] == 0:
#                 room_info[self.r][self.c] = 2
#                 self.clean += 1
#             can_move = False
#             for di in range(4):
#                 nr, nc = self.r + direction[di][0], self.c + direction[di][1]
#                 if nr < 0 or nc < 0 or nr >= R or nc >= C:
#                     continue
#                 if room_info[nr][nc] == 0:
#                     can_move = True
#                     break
#             if can_move:
#                 while not self.rotate():
#                     continue
#                 self.move_front()
#             elif self.move_back() == (-1, -1):
#                 break
#
#
# R, C = map(int, input().split(" "))
# # sd : 0 - 북  // 1- 동 // 2- 남 // 3- 서
# sr, sc, sd = map(int, input().split(" "))
# direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
# room_info = []
# for _ in range(R):
#     # 0 - 청소 x 빈칸 // 1- 벽
#     room_info.append(list(map(int, input().split(" "))))
#
# robot = Robot(sr, sc, sd)
# robot.run()
# print(robot.clean)
