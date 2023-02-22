techromino_list = [
    [[1, 1, 1, 1]],
    [[1],
     [1],
     [1],
     [1]],
    [[1, 1],
     [1, 1]],
    [[1, 0],
     [1, 0],
     [1, 1]],
    [[0, 1],
     [0, 1],
     [1, 1]],
    [[1, 1, 1],
     [1, 0, 0]],
    [[1, 1, 1],
     [0, 0, 1]],
    [[1, 1],
     [0, 1],
     [0, 1]],
    [[1, 1],
     [1, 0],
     [1, 0]],
    [[0, 0, 1],
     [1, 1, 1]],
    [[1, 0, 0],
     [1, 1, 1]],
    [[1, 0],
     [1, 1],
     [0, 1]],
    [[0, 1],
     [1, 1],
     [1, 0]],
    [[0, 1, 1],
     [1, 1, 0]],
    [[1, 1, 0],
     [0, 1, 1]],
    [[1, 1, 1],
     [0, 1, 0]],
    [[0, 1],
     [1, 1],
     [0, 1]],
    [[0, 1, 0],
     [1, 1, 1]],
    [[1, 0],
     [1, 1],
     [1, 0]],
]

R, C = map(int, input().split(" "))
map_info = []
result = 0
for _ in range(R):
    map_info.append(list(map(int, input().split(" "))))
for tech in techromino_list:
    tech_r_len, tech_c_len = len(tech), len(tech[0])
    for sr in range(R-tech_r_len+1):
        for sc in range(C-tech_c_len+1):
            tmp_sum = 0
            for tr in range(tech_r_len):
                for tc in range(tech_c_len):
                    tmp_sum += (map_info[sr+tr][sc+tc] * tech[tr][tc])
            result = max(result, tmp_sum)
print(result)

