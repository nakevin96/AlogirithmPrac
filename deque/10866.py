from sys import stdin


class Deque:
    def __init__(self):
        self.deque = [0 for _ in range(20002)]
        self.head = 10001
        self.tail = 10001

    def push_front(self, item):
        self.head -= 1
        self.deque[self.head] = item

    def push_back(self, item):
        self.deque[self.tail] = item
        self.tail += 1

    def pop_front(self):
        if self.head == self.tail:
            print(-1)
        else:
            print(self.deque[self.head])
            self.head += 1

    def pop_back(self):
        if self.head == self.tail:
            print(-1)
        else:
            print(self.deque[self.tail - 1])
            self.tail -= 1

    def empty(self):
        print(1 if self.head == self.tail else 0)

    def size(self):
        print(self.tail - self.head)

    def front(self):
        print(-1 if self.head == self.tail else self.deque[self.head])

    def back(self):
        print(-1 if self.head == self.tail else self.deque[self.tail - 1])


n = int(stdin.readline())
deque = Deque()
for _ in range(n):
    command = stdin.readline().rstrip().split(" ")
    if command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "pop_front":
        deque.pop_front()
    elif command[0] == "pop_back":
        deque.pop_back()
    elif command[0] == "size":
        deque.size()
    elif command[0] == "empty":
        deque.empty()
    elif command[0] == "front":
        deque.front()
    elif command[0] == "back":
        deque.back()
    else:
        print("wrong command")
