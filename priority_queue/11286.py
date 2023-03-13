import sys


class AbsHeap:
    def __init__(self):
        self.queue = [0 for _ in range(100001)]
        self.size = 0

    def push(self, x):
        self.size += 1
        self.queue[self.size] = x
        child = self.size
        while child > 1:
            parent = child // 2
            if abs(self.queue[child]) > abs(self.queue[parent]):
                break
            if abs(self.queue[child]) == abs(self.queue[parent]):
                if self.queue[child] >= self.queue[parent]:
                    break
            self.queue[child], self.queue[parent] = self.queue[parent], self.queue[child]
            child = parent

    def pop(self):
        if self.size == 0:
            return 0
        pop_val = self.queue[1]
        self.queue[1], self.queue[self.size] = self.queue[self.size], self.queue[1]
        self.size -= 1
        parent = 1
        while parent * 2  <= self.size:
            min_child = parent * 2
            if parent * 2 + 1 <= self.size:
                if abs(self.queue[parent * 2 + 1]) < abs(self.queue[parent * 2]):
                    min_child = parent * 2 + 1
                elif abs(self.queue[parent * 2 + 1]) == abs(self.queue[parent * 2]):
                    if self.queue[parent * 2 + 1] < self.queue[parent * 2]:
                        min_child = parent * 2 + 1
            if abs(self.queue[min_child]) > abs(self.queue[parent]):
                break
            if abs(self.queue[min_child]) == abs(self.queue[parent]):
                if self.queue[min_child] >= self.queue[parent]:
                    break
            self.queue[min_child], self.queue[parent] = self.queue[parent], self.queue[min_child]
            parent = min_child
        return pop_val


input = sys.stdin.readline
N = int(input())
heap = AbsHeap()
for _ in range(N):
    x = int(input())
    if x == 0:
        print(heap.pop())
    else:
        heap.push(x)
