'''
한나는 강원도 고랭지에서 유기농 배추를 재배하고자 한다
농약을 쓰지 않고 배추를 재배하기 위해서 배추를 해충으로부터 보호하는 것이 중요하기 때문에
한나는 배추 흰지렁이를 구매했다
배추를 보호하기 위해 구입해야 하는 배추 흰지렁이 수를 구해라
'''
from sys import stdin
from collections import deque

t = int(stdin.readline().rstrip())
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

for _t in range(t):
    m, n, k = map(int, stdin.readline().rstrip().split(" "))
    field_info = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    result = 0

    for _k in range(k):
        km, kn = map(int, stdin.readline().rstrip().split(" "))
        field_info[kn][km] = 1
        visited[kn][km] = 0

    for _n in range(n):
        for _m in range(m):
            if field_info[_n][_m] == 1 and visited[_n][_m] == 0:
                result += 1
                queue = deque([(_n, _m)])
                while queue:
                    curr_n, curr_m = queue.popleft()
                    if visited[curr_n][curr_m] != 0:
                        continue
                    visited[curr_n][curr_m] = 1
                    for i in range(4):
                        nn = curr_n + dn[i]
                        nm = curr_m + dm[i]
                        if nn < 0 or nm < 0 or nn >= n or nm >= m:
                            continue
                        if visited[nn][nm] == 0:
                            queue.append((nn, nm))

    print(result)
