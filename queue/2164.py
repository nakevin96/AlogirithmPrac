from sys import stdin


class Queue:
    def __init__(self, num=0):
        self.queue = [q for q in range(1, 1000002)]
        self.head = 0
        self.tail = num

    def size(self):
        return self.tail - self.head

    def popleft(self):
        tmp = self.queue[self.head]
        self.head += 1
        return tmp

    def append(self, item):
        self.queue[self.tail] = item
        self.tail += 1

    def front(self):
        return self.queue[self.head]


n = int(stdin.readline())
queue = Queue(n)

while queue.size() > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.front())
