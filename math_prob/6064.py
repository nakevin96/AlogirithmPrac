# 카잉 달력
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split(' '))
    candidates = [(M * i) + x for i in range(N)]
    flag = False
    for c in candidates:
        if y == N:
            if c % N == 0:
                flag = True
                print(c)
                break
        else:
            if c % N == y:
                flag = True
                print(c)
                break
    if not flag:
        print(-1)
