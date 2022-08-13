map_len = int(input())

map_info = []
rain_heights = set()
for row_idx in range(map_len):
    tmp = list(map(int, input().split()))
    rain_heights.update(set(tmp))
    map_info.append(tmp)
rain_heights = sorted(list(rain_heights))

result = 1
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def dfs(rain_height):
    answer = 0
    visited = [[0 for _c in range(map_len)] for _r in range(map_len)]

    for _r in range(map_len):
        for _c in range(map_len):
            if map_info[_r][_c] > rain_height and visited[_r][_c] == 0:
                answer += 1
                stack = list()
                stack.append((_r, _c))
                while stack:
                    curr_r, curr_c = stack.pop()
                    visited[curr_r][curr_c] = 1
                    for move_idx in range(4):
                        nr = curr_r + dr[move_idx]
                        nc = curr_c + dc[move_idx]
                        if nr < 0 or nr >= map_len or nc < 0 or nc >= map_len:
                            continue
                        elif map_info[nr][nc] > rain_height and visited[nr][nc] == 0:
                            stack.append((nr, nc))
    return answer


for height in rain_heights:
    result = max(result, dfs(height))

print(result)
