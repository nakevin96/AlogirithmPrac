import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for n in range(N):
    a, b, c, d = map(int, input().split(' '))
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB_dict = defaultdict(int)
for ai in range(N):
    for bi in range(N):
        AB_dict[A[ai] + B[bi]] += 1

result = 0
for ci in range(N):
    for di in range(N):
        target = (C[ci] + D[di]) * -1
        if target in AB_dict:
            result += AB_dict[target]
print(result)



