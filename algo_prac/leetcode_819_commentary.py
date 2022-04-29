# 입력값에는 대소문자가 섞여 있으며 쉽표 등 구두점이 존재한다.
# 따라서 데이터 클렌징이라 부르는 입력값에 대한 전처리 작업이 필요하다.
# 좀 더 편리하게 처리하기 위해 정규식을 섞어 쓰면 쉽게 처리 가능하다
from typing import List


def reorder_log_files(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters+digits

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(reorder_log_files(logs))


"""
람다 표현식이란 식별자 없이 실행 가능한 함수를 말하며
함수 선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있다.


"""