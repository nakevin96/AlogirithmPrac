from sys import stdin

s_input = stdin.readline

answer = 0
s = []
n = int(s_input())
while n > 0:
    n -= 1
    h = int(s_input())
    while s and s[-1] <= h:
        s.pop()
    answer += len(s)
    s.append(h)
print(answer)
