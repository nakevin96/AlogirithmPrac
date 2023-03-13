import sys

input = sys.stdin.readline


class Heap:
    def __init__(self):
        self.queue = [0 for _ in range(100001)]
        self.size = 0

    def switch_up_to_bottom(self, root):
        if root > self.size:
            return
        left, right = root * 2, (root * 2) + 1
        left_num = None if self.size < left else self.queue[left]
        right_num = None if self.size < right else self.queue[right]

        target = root
        if left_num and left_num < self.queue[target]:
            target = left
        if right_num and right_num < self.queue[target]:
            target = right

        if target == root:
            return
        self.queue[target], self.queue[root] = self.queue[root], self.queue[target]
        self.switch_up_to_bottom(target)

    def switch_bottom_to_up(self, child):
        if child == 1:
            return
        parent = child // 2
        if self.queue[parent] > self.queue[child]:
            self.queue[parent], self.queue[child] = self.queue[child], self.queue[parent]
            self.switch_bottom_to_up(parent)

    def push(self, x):
        self.size += 1
        self.queue[self.size] = x
        self.switch_bottom_to_up(self.size)

    def top(self):
        if self.size == 0:
            return None
        else:
            return self.queue[1]

    def pop(self):
        if self.size == 0:
            return 0
        pop_value = self.queue[1]
        self.queue[1], self.queue[self.size] = self.queue[self.size], self.queue[1]
        self.size -= 1
        self.switch_up_to_bottom(1)
        return pop_value


heap = Heap()
N = int(input())
for _ in range(N):
    n = int(input())
    if n >= 1:
        heap.push(n)
    else:
        print(heap.pop())
