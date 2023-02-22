class Robot:
    def __init__(self, start_r, start_c, start_direction):
        self.r = start_r
        self.c = start_c
        self.d = start_direction
        self.clean = 0
        self.d_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.db_list = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def move_front(self):
        nr, nc = self.r + self.d_list[self.d][0], self.c + self.d_list[self.d][1]
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            return -1, -1
        if room_info[nr][nc] == 0:
            self.r, self.c = nr, nc
            return self.r, self.c
        return -1, -1

    def move_back(self):
        nr, nc = self.r + self.db_list[self.d][0], self.c + self.db_list[self.d][1]
        if nr < 0 or nc < 0 or nr >= R or nc >= C:
            return -1, -1
        if room_info[nr][nc] != 1:
            self.r, self.c = nr, nc
            return self.r, self.c
        return -1, -1

    def rotate(self):
        if self.d == 0:
            self.d = 3
        else:
            self.d -= 1
        nr, nc = self.r + self.d_list[self.d][0], self.c + self.d_list[self.d][1]
        if (0 <= nr < R and 0 <= nc < C) and room_info[nr][nc] == 0:
            return True
        return False

    def run(self):
        while True:
            if room_info[self.r][self.c] == 0:
                room_info[self.r][self.c] = 2
                self.clean += 1
            can_move = False
            for di in range(4):
                nr, nc = self.r + direction[di][0], self.c + direction[di][1]
                if nr < 0 or nc < 0 or nr >= R or nc >= C:
                    continue
                if room_info[nr][nc] == 0:
                    can_move = True
                    break
            if can_move:
                while not self.rotate():
                    continue
                self.move_front()
            elif self.move_back() == (-1, -1):
                break


R, C = map(int, input().split(" "))
# sd : 0 - 북  // 1- 동 // 2- 남 // 3- 서
sr, sc, sd = map(int, input().split(" "))
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
room_info = []
for _ in range(R):
    # 0 - 청소 x 빈칸 // 1- 벽
    room_info.append(list(map(int, input().split(" "))))

robot = Robot(sr, sc, sd)
robot.run()
print(robot.clean)
