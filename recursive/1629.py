'''
자연수 A를 B번 곱한 수를 알고 싶다
단 구하려는 수가 매우 커질 수 있기 때문에 C로 나눈 나머지를 구하라
'''

from sys import stdin


def solution():
    def divide(da, db, dc):
        if db == 1:
            return da % dc
        tmp = divide(da, db // 2, dc)
        if db % 2 == 0:
            return (tmp * tmp) % dc
        else:
            return (tmp * tmp * da) % dc

    a, b, c = map(int, stdin.readline().rstrip().split(" "))
    return divide(a, b, c)


print(solution())
