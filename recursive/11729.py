N = int(input())


def hanoi(n, pos, target, non_target):
    if n == 1:
        return [(pos, target)]
    result = []
    result.extend(hanoi(n - 1, pos, non_target, target))
    result.extend(hanoi(1, pos, target, non_target))
    result.extend(hanoi(n - 1, non_target, target, pos))
    return result


sol = hanoi(N, 1, 3, 2)
print(len(sol))
for s1, s2 in sol:
    print(f"{s1} {s2}")
