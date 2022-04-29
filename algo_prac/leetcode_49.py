# 문자열 배열을 받아 애너그램 단위로 그룹핑하라
# 애너그램이란 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.
from typing import List


def anagram(word_list: List[str]):
    anagram_group = []
    word_dict = {}
    word_tmp = []
    for word in word_list:
        word_tmp.append(sorted(list(word)))

    for idx in range(len(word_tmp)):
        if ''.join(word_tmp[idx]) not in word_dict:
            word_dict[''.join(word_tmp[idx])] = [word_list[idx]]
        else:
            word_dict[''.join(word_tmp[idx])].append(word_list[idx])

    return list(word_dict.values())


input_word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram(input_word_list))
