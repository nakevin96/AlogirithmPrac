from collections import deque

direction_dict = {
    1: 'clockwise',
    -1: 'counterclockwise'
}

pole_dict = {
    '0': 'N',
    '1': 'S',
}


class Gear:
    def __init__(self, info):
        self.info = deque(info)
        self.left_gear = None
        self.right_gear = None

    def get_left_pole(self):
        return self.info[6]

    def get_right_pole(self):
        return self.info[2]

    def rotate(self, direction):
        if direction != -1 and direction != 1:
            return
        if direction_dict[direction] == 'clockwise':
            self.info.appendleft(self.info.pop())
        elif direction_dict[direction] == 'counterclockwise':
            self.info.append(self.info.popleft())

    def spread_rotate(self, direction, spread_direction):
        if spread_direction == 'left':
            if self.left_gear is not None:
                if self.left_gear.get_right_pole() != self.get_left_pole():
                    self.left_gear.spread_rotate(-1*direction, 'left')
                    self.left_gear.rotate(-1 * direction)
        elif spread_direction == 'right':
            if self.right_gear is not None:
                if self.right_gear.get_left_pole() != self.get_right_pole():
                    self.right_gear.spread_rotate(-1*direction, 'right')
                    self.right_gear.rotate(-1*direction)


gear_list = []
for _ in range(4):
    gear_list.append(Gear(list(input())))

for i in range(4):
    if i > 0:
        gear_list[i].left_gear = gear_list[i-1]
    if i < 3:
        gear_list[i].right_gear = gear_list[i+1]

K = int(input())
for _ in range(K):
    gear_no, rotate_direction = map(int, input().split(' '))
    gear_no -= 1
    curr_gear = gear_list[gear_no]
    curr_gear.spread_rotate(rotate_direction, 'left')
    curr_gear.spread_rotate(rotate_direction, 'right')
    curr_gear.rotate(rotate_direction)

result = 0
for i in range(4):
    if pole_dict[gear_list[i].info[0]] == 'S':
        result += (2**i)

print(result)
