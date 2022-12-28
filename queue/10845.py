from sys import stdin

s_input = stdin.readline


class Queue:
    def __init__(self):
        self.queue = [0 for _ in range(100001)]
        self.head = 0
        self.tail = 0

    def push(self, num):
        self.queue[self.tail] = num
        self.tail += 1

    def pop(self):
        print("-1" if self.head == self.tail else self.queue[self.head])
        if self.head < self.tail:
            self.head += 1

    def size(self):
        print(self.tail - self.head)

    def empty(self):
        print("1" if self.head == self.tail else "0")

    def front(self):
        print(self.queue[self.head] if self.head < self.tail else "-1")

    def back(self):
        print(self.queue[self.tail - 1] if self.head < self.tail else "-1")


n = int(s_input())
queue = Queue()

for _ in range(n):
    command = s_input().rstrip().split(" ")
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
