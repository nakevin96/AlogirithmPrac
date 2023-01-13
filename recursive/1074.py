'''
크기가 2^n * 2^n인 배열을 Z모양으로 탐색하려고 한다.
'''

n, r, c = map(int, input().split(" "))


def solution(cn, cr, cc):
    if cn == 1:
        if cr == 0 and cc == 0:
            return 0
        elif cr == 0 and cc == 1:
            return 1
        elif cr == 1 and cc == 0:
            return 2
        elif cr == 1 and cc == 1:
            return 3

    criterion = 2 ** (cn - 1)
    if cr < criterion and cc < criterion:
        return solution(cn - 1, cr, cc)
    elif cr < criterion <= cc:
        return (criterion * criterion) + solution(cn - 1, cr, cc - criterion)
    elif cr >= criterion > cc:
        return (criterion * criterion) * 2 + solution(cn - 1, cr - criterion, cc)
    elif cr >= criterion and cc >= criterion:
        return (criterion * criterion) * 3 + solution(cn - 1, cr - criterion, cc - criterion)


print(solution(n, r, c))
