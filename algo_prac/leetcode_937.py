# 로그를 재정렬 하라, 기준은 다음과 같다
# 로그의 가장 앞 부분은 식별자이다.
# 문자로 구성된 로그가 숫자보다 앞에 온다
# 식별자는 순서에 영향을 및치 않지만 문자가 동일하면 식별자 순으로 한다
# 숫자 로그는 입력 순으로한다
from typing import List


def sort_logs(log_list: List[str]):
    split_log_list = []
    for log in log_list:
        split_log_list.append(log.split(' '))

    str_log = []
    num_log = []
    for log in split_log_list:
        if log[1].isdigit():
            num_log.append(log)
        else:
            str_log.append(log)

    str_log.sort(key=lambda x: (x[1:], x[0]))
    return str_log + num_log


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
log_sorted = sort_logs(logs)
print(log_sorted)
