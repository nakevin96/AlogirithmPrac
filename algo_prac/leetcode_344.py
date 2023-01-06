# 문자열을 뒤집는 함수를 작성하라, 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라

def reverse_string(input_s: str):
    s_list = list(input_s)
    s_list.reverse()
    print(s_list)


input_string = input()
reverse_string(input_string)
