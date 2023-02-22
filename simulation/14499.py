class Dice:
    def __init__(self, r, c):
        self.info = [[0 for _ in range(3)] for _ in range(4)]
        self.r = r
        self.c = c

    def get_pos(self):
        return self.r, self.c

    def update_bottom(self, val):
        self.info[1][1] = val

    def get_bottom(self):
        return self.info[1][1]

    def get_top(self):
        return self.info[3][1]

    def roll(self, direction):
        if direction == 1:
            # 동쪽
            if self.c + 1 >= M:
                return False
            self.c += 1
            target = [self.info[3][1], self.info[1][0], self.info[1][1], self.info[1][2]]
            self.info[3][1], self.info[1][0] = target[1], target[2]
            self.info[1][1], self.info[1][2] = target[3], target[0]
            return True
        elif direction == 2:
            # 서쪽
            if self.c - 1 < 0:
                return False
            self.c -= 1
            target = [self.info[3][1], self.info[1][0], self.info[1][1], self.info[1][2]]
            self.info[3][1], self.info[1][0] = target[3], target[0]
            self.info[1][1], self.info[1][2] = target[1], target[2]
            return True
        elif direction == 3:
            # 북쪽
            if self.r - 1 < 0:
                return False
            self.r -= 1
            target = [self.info[3][1], self.info[2][1], self.info[1][1], self.info[0][1]]
            self.info[3][1], self.info[2][1] = target[1], target[2]
            self.info[1][1], self.info[0][1] = target[3], target[0]
            return True
        else:
            # 남쪽
            if self.r + 1 >= N:
                return False
            self.r += 1
            target = [self.info[3][1], self.info[2][1], self.info[1][1], self.info[0][1]]
            self.info[3][1], self.info[2][1] = target[3], target[0]
            self.info[1][1], self.info[0][1] = target[1], target[2]
            return True


N, M, X, Y, K = map(int, input().split(" "))
dice = Dice(X, Y)
map_info = []
for _ in range(N):
    map_info.append(list(map(int, input().split(" "))))
command_info = list(map(int, input().split(" ")))
for ki in range(K):
    if dice.roll(command_info[ki]):
        print(dice.get_top())
        curr_r, curr_c = dice.get_pos()
        if map_info[curr_r][curr_c] == 0:
            map_info[curr_r][curr_c] = dice.get_bottom()
        else:
            dice.update_bottom(map_info[curr_r][curr_c])
            map_info[curr_r][curr_c] = 0

