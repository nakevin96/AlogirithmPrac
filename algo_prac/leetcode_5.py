# 가장 긴 팰린드롬 부분 문자열을 출력하라.
def longest_palindrome(s: str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s) - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

    return result


def main():
    user_input = "babad"
    print(longest_palindrome(user_input))


if __name__ == "__main__":
    main()
