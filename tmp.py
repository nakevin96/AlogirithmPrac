import math


def solution(target):
    THROW_COUNT, VALID_COUNT = 0, 1
    valid_table = [i for i in range(1, 21)]
    valid_table.append(50)
    invalid_table = [i * 2 for i in range(1, 21) if i * 2 > 20]
    invalid_table.extend([i * 3 for i in range(1, 31) if i * 3 > 20])
    invalid_table = list(set(invalid_table))

    dt = [[math.inf, 0] for _ in range(target + 1)]
    dt[0][THROW_COUNT] = 0

    for t in range(1, target + 1):
        for v in valid_table:
            if t - v < 0:
                continue

            tmp_throw = dt[t - v][THROW_COUNT] + 1
            tmp_valid = dt[t - v][VALID_COUNT] + 1

            if tmp_throw < dt[t][THROW_COUNT]:
                dt[t] = [tmp_throw, tmp_valid]
            elif tmp_throw == dt[t][THROW_COUNT]:
                dt[t][VALID_COUNT] = max(tmp_valid, dt[t][VALID_COUNT])

        for iv in invalid_table:
            if t - iv < 0:
                continue

            tmp_throw = dt[t - iv][THROW_COUNT] + 1
            tmp_valid = dt[t - iv][VALID_COUNT]

            if tmp_throw < dt[t][THROW_COUNT]:
                dt[t] = [tmp_throw, tmp_valid]
            elif tmp_throw == dt[t][THROW_COUNT]:
                dt[t][VALID_COUNT] = max(tmp_valid, dt[t][VALID_COUNT])
    return dt[target]

print(solution(106))
