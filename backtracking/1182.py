'''
N개의 정수로 이루어진 수열이 있을 때
크기가 양수인 부분수열 중
수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하라.
'''

# 과거 풀이
# result = 0
# currSum = 0
# N, S = map(int, input())
# num_list = sorted(list(map(int, input().split(" "))))
#
#
# def sol(curr):
#     global result, currSum
#     if curr == N:
#         return
#     if currSum + num_list[curr] == S:
#         result += 1
#
#     sol(curr + 1)
#     currSum += num_list[curr]
#     sol(curr + 1)
#     currSum -= num_list[curr]
#
#
# sol(0)
# print(result)

# 2023 02 17 다시풀기
#1 brute force 접근
def sol1():
    N, S = map(int, input().split(" "))
    N_list = list(map(int, input().split(" ")))
    def make_candidates(c_list, count):
        if count == 0:
            return [[]]
        result = []
        for i in range(len(c_list)):
            item = c_list[i]
            for rest in make_candidates(c_list[i+1:], count-1):
                result.append([item, *rest])

        return result

    result = 0
    for select_num in range(1, N+1):
        candidates = make_candidates(N_list, select_num)
        for c in candidates:
            if sum(c) == S:
                result += 1
    return result

print(sol1())