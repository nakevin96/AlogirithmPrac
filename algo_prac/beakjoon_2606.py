from collections import defaultdict
com_num = int(input())
com_pair_num = int(input())

com_pair_dict = defaultdict(list)
for _ in range(com_pair_num):
    _c1, _c2 = map(int, input().split())
    com_pair_dict[_c2].append(_c1)
    com_pair_dict[_c1].append(_c2)

visited = [0] * (com_num+1)
stack = [1]
result = -1
while stack:
    curr_com = stack.pop()
    visited[curr_com] = 1
    result += 1
    for next_com in com_pair_dict[curr_com]:
        if not visited[next_com] and next_com not in stack:
            stack.append(next_com)

print(result)
