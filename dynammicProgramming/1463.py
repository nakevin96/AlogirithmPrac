from collections import deque

N = int(input())


def sol(n):
    qs = set()
    queue = deque([(1, 0)])
    while queue:
        curr_n, step = queue.popleft()
        qs.add(curr_n)
        if curr_n == n:
            return step
        if curr_n+1 not in qs:
            queue.append((curr_n + 1, step + 1))
        if curr_n*2 not in qs:
            queue.append((curr_n * 2, step + 1))
        if curr_n*3 not in qs:
            queue.append((curr_n * 3, step + 1))


print(sol(N))
