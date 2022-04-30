# leetcode 49번에 대한 해설

# 애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는것
# sorted는 문자열도 잘 정렬하며 결과를 리스트 형태로 리턴
# 이를 키로 사용하기 위해 join()으로 합쳐 이값을 키로 하는 딕셔너리로 구성
import collections
from typing import List


def group_anagrams1(strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


a = [2, 5, 1, 9, 7]
a.sort()
print(a)
b = "zbkdjif"
print("".join(sorted(b)))
