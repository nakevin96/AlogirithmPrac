'''
최백준 조교가 방 열쇠를 주머니에 넣은 채 서울로 가서
702에 새로운 보안 시스템을 설치하기로 했다
암호로 동작하며
암호는 서로 다른 L개의 알파벳 소문자로 구성되며
최소 1개의 모음과 최소 2개의 자음으로 구성된다
또한 정렬된 문자열을 선호하는 조교들은 암호를 이루는 알파벳이
사전순에 맞게 조작하였다.

새 보안시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 c가지 있다고 한다.
조교 방에 들어가기위해 c개의 문자가 주어진 상황에서 가능성있는 모든 암호를 구해라
'''

result = 0
L, C = map(int, input().split(" "))
curr_list = []
alpha_list = sorted(input().split(" "))


def sol(idx, vowel_num, consonant_num):
    global result
    if idx > C:
        return
    if vowel_num + consonant_num == L:
        if vowel_num >= 1 and consonant_num >= 2:
            print("".join(curr_list))
        return

    for i in range(idx, C):
        curr_list.append(alpha_list[i])
        if alpha_list[i] in {'a', 'e', 'i', 'o', 'u'}:
            sol(i + 1, vowel_num + 1, consonant_num)
        else:
            sol(i + 1, vowel_num, consonant_num + 1)
        curr_list.pop()


sol(0, 0, 0)
