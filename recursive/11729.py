'''
3개의 장대가 있고 반경이 다른 서로 다른 n개의 원판이 존재한다
원판은 반경이 큰 순서로 쌓여있으며 3번째 장대로 옮기려한다
- 한번에 한개의 원판만을 옮길 수 있다
- 항상 위 원판이 아래 원판보다 작아야 한다.
'''

k = int(input())


def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)


sum = 1
for i in range(k - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(k, 1, 2, 3)
