'''
흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리라는 방법이 있다
흰점은 0 검은 점은 1로만 이루어져 있다
0과 1이 섞여있으면 왼쪽 위 오른쪽 위 왼쪽 아래 오른쪽 아래 이렇게 4개의 영상으로 나누어 압축하며
압축 결과를 괄호안에 욲어 표현한다.
'''
from sys import stdin

N = int(stdin.readline().rstrip())
video_info = []
for _ in range(N):
    video_info.append(list(map(int, list(stdin.readline().rstrip()))))


def video_sol(cn, cr, cc):
    if cn == 1:
        return str(video_info[cr][cc])
    bit = video_info[cr][cc]
    is_done = True
    for _r in range(cn):
        for _c in range(cn):
            if video_info[cr + _r][cc + _c] != bit:
                is_done = False
                break
    if is_done:
        return str(bit)
    else:
        tmp_result = "("
        nn = cn // 2
        for nr in range(2):
            for nc in range(2):
                tmp_result += video_sol(nn, cr + (nr * nn), cc + (nc * nn))
        tmp_result += ")"
        return tmp_result


print(video_sol(N, 0, 0))
