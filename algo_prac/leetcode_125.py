# 주어진 문자열이 팰린드롬인지 확인하라.
# 대 소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 입력 : A man, a plan ,a canal: Panama
# 출력 : True

# 팰린드롬이란 뒤집어도 같은 말이 되는 단어 혹은 문장
import re

print("write your test text for palindrome :")
test_text = input()

test_text = test_text.lower()
test_text = test_text.strip()
test_text = test_text.replace(' ', '')
test_text = re.findall('[a-zA-Z0-9]', test_text)

test_text = list(test_text)
reversed_text = list(reversed(test_text))

print(f'{test_text == reversed_text}')
