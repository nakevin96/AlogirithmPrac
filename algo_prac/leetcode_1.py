# 덧셈을 하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
from itertools import combinations


def get_index_list(num_list, target_num):
    comb = combinations(num_list, 2)
    comb_sum_dict = {}
    for item1, item2 in comb:
        if item1 + item2 not in comb_sum_dict:
            comb_sum_dict[item1+item2] = [item1, item2]

    if target_num in comb_sum_dict:
        result_value = comb_sum_dict[target_num]
        return [num_list.index(result_value[0]), num_list.index(result_value[1])]
    else:
        return None


print(get_index_list([2, 7, 11, 15], 9))
