# # N개의 시험장, i번 응시자 수 Ai
#
# # 감독관은 총감독, 부감독 존재
# # 총감독 B명 감시, 부감독 C명 감시
#
# # 총감독은 1명, 부감독은 여러명
#
# # 모든 응시생이 감시되어야 함
# # 필요한 감독관 수 최솟값
# from sys import stdin
#
# input = stdin.readline
#
# N = int(input())
#
# student_num_list = list(map(int, input().rstrip().split(' ')))
#
# B, C = map(int, input().split())
#
# result = 0
# for student_num in student_num_list:
#     tmp_result = 1
#     tmp_store = student_num - B
#     if tmp_store > 0:
#         tmp_result += (tmp_store // C)
#         tmp_store %= C
#
#     if tmp_store > 0:
#         tmp_result += 1
#
#     result += tmp_result
#
# print(result)

from sys import stdin
import math

input = stdin.readline

N = int(input())
student_num_list = list(map(int, input().rstrip().split(' ')))
B, C = map(int, input().split())
def get_val(target_num):
    return 1 if target_num - B <= 0 else 1 + math.ceil((target_num-B)/C)
print(sum(list(map(get_val, student_num_list))))
