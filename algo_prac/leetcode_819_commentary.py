# 입력값에는 대소문자가 섞여 있으며 쉽표 등 구두점이 존재한다.
# 따라서 데이터 클렌징이라 부르는 입력값에 대한 전처리 작업이 필요하다.
# 좀 더 편리하게 처리하기 위해 정규식을 섞어 쓰면 쉽게 처리 가능하다
import collections
from typing import List
import re


def most_common_word(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

    counts = collections.Counter(words)

    print(counts)
    print(counts.most_common(1))
    print(counts.most_common(1)[0])
    return counts.most_common(1)[0][0]


p = "Bob hit a ball, the hit BALL flew far after it was hit."
ban = ["hit"]

print(most_common_word(p, ban))
