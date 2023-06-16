# 홍준이 주식에 빠져있음
# 미래를 보는 눈이 뛰어나 주가를 예측 가능
# 1. 주식을 사거나 2. 원하는 양만큼 팔거나 3. 아무 행동도 취하지 않을 수 있다.
from sys import stdin

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    stock_val_list = list(map(int, stdin.readline().rstrip().split(' ')))

    result = 0
    while stock_val_list:
        curr_stock = stock_val_list.pop()
        while stock_val_list and stock_val_list[-1] < curr_stock:
            result += (curr_stock - stock_val_list[-1])
            stock_val_list.pop()
        if not stock_val_list:
            break

    print(result)
