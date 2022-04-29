# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며 구두점 또한 무시
from typing import List
import re


def frequent_word_without_banned(paragraph_input: str, ban_list: List[str]):
    paragraph_list = paragraph_input.lower().split()
    paragraph_modified = []
    for word in paragraph_list:
        paragraph_modified.append(re.sub('[^a-z]', "", word))

    paragraph_count = {}
    for word in paragraph_modified:
        if word in ban_list:
            continue
        if word in paragraph_count:
            paragraph_count[word] += 1
        else:
            paragraph_count[word] = 1
    result = max(paragraph_count, key=paragraph_count.get)
    return result


# 입력
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(frequent_word_without_banned(paragraph, banned))
