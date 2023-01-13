'''
재귀적 패턴으로 별을 찍어 보자.
N이 3의 거듭제곱 꼴로 주어질 때 N의 패턴은 NxN 정사각형 모양이다
크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 카넹 별이 하나씩 존재한다.
'''

N = int(input())
data = [["" for _ in range(N)] for _ in range(N)]


def recursive_star(n, r, c, flag):
    if flag:
        for fr in range(n):
            for fc in range(n):
                data[r + fr][c + fc] = " "
        return
    if n == 1:
        data[r][c] = "*"
        return
    for _r in range(3):
        for _c in range(3):
            if _r == 1 and _c == 1:
                recursive_star(n // 3, r + (n // 3), c + (n // 3), True)
            else:
                recursive_star(n // 3, r + (_r * (n // 3)), c + (_c * (n // 3)), False)
    return


recursive_star(N, 0, 0, False)
for d in data:
    print("".join(d))
