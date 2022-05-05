# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.
from itertools import combinations


def three_sum(nums):
    three_bind_lists = list(combinations(nums, 3))
    answer_dict = {}
    for three_bind_list in three_bind_lists:
        answer_dict[tuple(three_bind_list)] = sum(three_bind_list)

    sum_0_answer_unsort = map(list, dict(filter(lambda x: x[1] == 0, answer_dict.items())).keys())
    sum_0_answer_sort = []
    for item in sum_0_answer_unsort:
        sorted_item = sorted(item)
        if sorted_item in sum_0_answer_sort:
            continue
        sum_0_answer_sort.append(sorted_item)
    return sum_0_answer_sort


print(three_sum([-1, 0, 1, 2, -1, -4]))
