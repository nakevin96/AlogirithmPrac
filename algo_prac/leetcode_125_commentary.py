# 직접 문자열을 받아 팰린드롬 여부를 판별한다
# 대소문자 여부를 구분하지 않으며 영문자, 숫자만을 대상으로 한다는 조건이 있다
# 따라서 이 부분에 대한 전처리 부터 구현한다.

"""풀이 1
def is_palindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


user_input = input()
print(is_palindrome(user_input))
"""

"""풀이 2"""

# import collections
#
#
# def is_palindrome(s: str) -> bool:
#     strs = collections.deque()
#
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#
#     return True
#
#
# user_input = input()
# print(is_palindrome(user_input))
import re


def is_palindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


user_input = input()
print(is_palindrome(user_input))
