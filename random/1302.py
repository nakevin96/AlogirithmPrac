# 베스트 셀러 https://www.acmicpc.net/problem/1302
from sys import stdin

input = stdin.readline

N = int(input())

book_dict = dict()
for _ in range(N):
    book_name = input().rstrip()
    if book_name in book_dict:
        book_dict[book_name] += 1
    else:
        book_dict[book_name] = 1

book_list = sorted([(-count, book_name) for book_name, count in book_dict.items()])
print(book_list[0][1])
