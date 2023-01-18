'''
독일 로또는 1 ~ 49까지의 수 중 6개를 고른다.
가장 유명한 전략은 49개의 수 중 k개의 수를 골라 집합 S를 만든 후 그 수만 가지고 번호를 선택하는 것이다.
집합 S와 K가 주어졌을 때 수를 고르는 모든 방법을 구하시오
'''
from sys import stdin


def sol(num_list, count):
    sol_result = []
    if count == 0:
        return [[]]
    for idx in range(len(num_list)):
        item = num_list[idx]
        rest = num_list[idx + 1:]
        for tmp_result in sol(rest, count - 1):
            sol_result.append([item, *tmp_result])
    return sol_result


while True:
    n_list = list(map(int, stdin.readline().rstrip().split(" ")))
    if n_list[0] == 0:
        break
    result = sol(n_list[1:], 6)
    for r in result:
        print(" ".join(map(str, r)))
    print("")
