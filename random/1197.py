# 최소 스패닝 트리: https://www.acmicpc.net/problem/1197
import sys

input = sys.stdin.readline
# 1. 입력받은 간선에 대한 정보를 코스트가 낮은 순서로 정렬한다.
V, E = map(int, input().rstrip().split(' '))
E_info = []
for _ in range(E):
    E_info.append(list(map(int, input().rstrip().split(' '))))

E_info.sort(key=lambda x: x[2])

# 2. 낮은 순으로 절열된 코스트를 순서대로 순환하며, 사이클이 형성되지 않을 경우 result에 더해준다.
# 2-1. 사이클이 있는지 판단하는 알고리즘으로 Union Find 알고리즘을 적용한다.
# 2-2. Union Find의 경우 Parent배열을 선언하여 i, j에 대해 Parent[i] == Parent[j]이면 사이클이라 판단한다
result = 0
parent = [i for i in range(V + 1)]


def get_parent_node(curr_node):
    target_child_nodes = []
    while parent[curr_node] != curr_node:
        target_child_nodes.append(curr_node)
        curr_node = parent[curr_node]
    for target_child_node in target_child_nodes:
        parent[target_child_node] = curr_node
    return curr_node


for v1, v2, cost in E_info:
    v1 = get_parent_node(v1)
    v2 = get_parent_node(v2)
    if v1 == v2:
        continue
    else:
        result += cost
        if v1 < v2:
            parent[v2] = v1
        else:
            parent[v1] = v2

        # 3. result를 출력한다.
print(result)
