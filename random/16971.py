# 배열 b의 값: https://www.acmicpc.net/problem/16971
import sys

input = sys.stdin.readline

n, m = tuple(map(int, input().split()))
board = [
    list(map(int, input().split()))
    for _ in range(n)
]
row_sum = [0 for _ in range(n)]
col_sum = [0 for _ in range(m)]


def getRowSum(row):
    return board[row][0] + board[row][m - 1] + 2 * sum(board[row][1: m - 1])


def getColSum(col):
    return board[0][col] + board[n - 1][col] + 2 * sum([board[i][col] for i in range(1, n - 1)])


for i in range(n):
    if i == 0 or i == n - 1:
        row_sum[i] = getRowSum(i)
    else:
        row_sum[i] = 2 * getRowSum(i)

for i in range(m):
    if i == 0 or i == m - 1:
        col_sum[i] = getColSum(i)
    else:
        col_sum[i] = 2 * getColSum(i)

result = sum(row_sum)
min_row_val, min_col_val = float('inf'), float('inf')
for i in range(1, n - 1):
    if min_row_val > row_sum[i]:
        min_row_val = row_sum[i]

for i in range(1, m - 1):
    if min_col_val > col_sum[i]:
        min_col_val = col_sum[i]

print(max(result, result + row_sum[0] - (min_row_val // 2), result + row_sum[-1] - (min_row_val // 2),
          result + col_sum[0] - (min_col_val // 2), result + col_sum[-1] - (min_col_val // 2)))