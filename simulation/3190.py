from collections import deque


class Snake:
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, map_info):
        self.body = deque([(0, 0)])
        self.d = 1
        self.t = 0
        self.map_info = map_info

    def rotate_cw(self):
        if self.d == 3:
            self.d = 0
        else:
            self.d += 1

    def rotate_ccw(self):
        if self.d == 0:
            self.d = 3
        else:
            self.d -= 1

    def move(self):
        self.t += 1
        hr, hc = self.body[0][0], self.body[0][1]
        nhr, nhc = hr + Snake.direction[self.d][0], hc + Snake.direction[self.d][1]
        # 다음 칸이 벽
        if nhr < 0 or nhc < 0 or nhr >= N or nhc >= N:
            return False
        # 다음 칸이 내 몸
        if self.map_info[nhr][nhc] == 2:
            return False
        # 아니면 머리 다음칸에 위치
        self.body.appendleft((nhr, nhc))
        # 사과가 없으면 몸길이 줄임 있으면 꼬리 유지
        if self.map_info[nhr][nhc] == 0:
            tr, tc = self.body.pop()
            self.map_info[tr][tc] = 0
        self.map_info[nhr][nhc] = 2
        return True


N = int(input())
Map_info = [[0 for _ in range(N)] for _ in range(N)]
Map_info[0][0] = 2
apple_num = int(input())
for _ in range(apple_num):
    ar, ac = map(int, input().split(" "))
    Map_info[ar-1][ac-1] = 1

schedule_num = int(input())
schedule_list = deque()
for _ in range(schedule_num):
    schedule_list.append(input().split(" "))

snake = Snake(Map_info)
while True:
    if not snake.move():
        break
    schedule_time, rotate_direction = None, None
    if schedule_list:
        schedule_time, rotate_direction = schedule_list[0][0], schedule_list[0][1]
    if schedule_time is not None and snake.t == int(schedule_time):
        schedule_list.popleft()
        if rotate_direction == 'L':
            snake.rotate_ccw()
        else:
            snake.rotate_cw()

print(snake.t)
