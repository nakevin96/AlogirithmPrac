# 공유기 설치: https://www.acmicpc.net/problem/2110
import sys

input = sys.stdin.readline

N, C = map(int, input().split(' '))
house_list = []
for _ in range(N):
    house_list.append(int(input()))
house_list.sort()

left, right = 0, 1000000000
while left < right:
    mid = (left + right + 1) // 2
    curr_pos = 0
    count = 0
    for h in house_list:
        if h >= curr_pos:
            count += 1
            curr_pos = h + mid
    if count >= C:
        left = mid
    else:
        right = mid - 1
print(left)
