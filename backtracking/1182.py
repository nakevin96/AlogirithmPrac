'''
N개의 정수로 이루어진 수열이 있을 때
크기가 양수인 부분수열 중
수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하라.
'''

result = 0
currSum = 0
N, S = map(int, input())
num_list = sorted(list(map(int, input().split(" "))))


def sol(curr):
    global result, currSum
    if curr == N:
        return
    if currSum + num_list[curr] == S:
        result += 1

    sol(curr + 1)
    currSum += num_list[curr]
    sol(curr + 1)
    currSum -= num_list[curr]


sol(0)
print(result)
