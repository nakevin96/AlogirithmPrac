import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline
N, M, V = map(int, input().split(' '))
next_node_dict = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split(' '))
    next_node_dict[u].append(v)
    next_node_dict[v].append(u)


def bfs(s_node):
    result = []
    visited = set()
    visited.add(s_node)
    queue = deque([s_node])
    while queue:
        curr_node = queue.popleft()
        result.append(str(curr_node))
        next_node_list = next_node_dict[curr_node]
        for next_node in sorted(next_node_list):
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)

    print(' '.join(result))


def dfs(d_node):
    visited = set()
    result = []
    stack = [d_node]

    while stack:
        curr_node = stack.pop()
        if curr_node in visited:
            continue
        visited.add(curr_node)
        result.append(str(curr_node))
        next_node_list = next_node_dict[curr_node]
        for next_node in sorted(next_node_list, reverse=True):
            if next_node not in visited:
                stack.append(next_node)
    print(' '.join(result))


dfs(V)
bfs(V)
