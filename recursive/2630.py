'''
정사각형 칸으로 이루어진 정사각형 종이가 주어진다
정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다.
주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 종이를 만들려 한다.
'''
from sys import stdin

n = int(stdin.readline().rstrip())
result = [0, 0]
paper_info = []
for _ in range(n):
    paper_info.append(list(map(int, stdin.readline().rstrip().split(" "))))


def paper_sol(cn, cr, cc):
    if cn == 1:
        result[paper_info[cr][cc]] += 1
        return
    base = paper_info[cr][cc]
    is_done = True
    for _r in range(cn):
        for _c in range(cn):
            if paper_info[cr + _r][cc + _c] != base:
                is_done = False
                break
    if is_done:
        result[base] += 1
    else:
        nn = cn // 2
        for nr in range(2):
            for nc in range(2):
                paper_sol(nn, cr + (nr * nn), cc + (nc * nn))


paper_sol(n, 0, 0)
print(result[0])
print(result[1])
