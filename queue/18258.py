from sys import stdin


class Queue:
    def __init__(self):
        self.queue = [0 for _ in range(2000001)]
        self.head = 0
        self.tail = 0

    def push(self, num):
        self.queue[self.tail] = num
        self.tail += 1

    def pop(self):
        if self.head == self.tail:
            print("-1")
        else:
            print(self.queue[self.head])
            self.head += 1

    def size(self):
        print(self.tail - self.head)

    def empty(self):
        print(1 if self.head == self.tail else 0)

    def front(self):
        print(-1 if self.head == self.tail else self.queue[self.head])

    def back(self):
        print(-1 if self.head == self.tail else self.queue[self.tail - 1])


n = int(stdin.readline())
queue = Queue()

for _ in range(n):
    command = stdin.readline().rstrip().split(" ")
    if command[0] == "push":
        queue.push(command[1])
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "empty":
        queue.empty()
    elif command[0] == "front":
        queue.front()
    elif command[0] == "back":
        queue.back()
    else:
        print("wrong command")
