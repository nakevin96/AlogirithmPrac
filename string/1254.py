# 팰린드롬 만들기: https://www.acmicpc.net/problem/1254

# 긴문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 함

input_string = list(input())
modified_string = list('?'.join(input_string))
m_len = len(modified_string)
mid = m_len // 2

while True:
    left, right = mid - 1, mid + 1

    while left >= 0 and right < m_len and modified_string[left] == modified_string[right]:
        left -= 1
        right += 1

    if right >= m_len:
        right -= 1
        left_most = 2 * mid - right - 1
        result = right - mid + 1
        # if modified_string[mid] == '?':
        #     result += (right - mid) + 1
        # else:
        #     result += (right - mid)
        if left_most >= 0:
            result += (left_most + 1)
        print(result)
        break

    mid += 1
