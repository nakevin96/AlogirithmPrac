# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라.

# memory out, time out 나서 폐기
# from itertools import combinations
#
#
# def three_sum(nums):
#     three_bind_lists = list(combinations(nums, 3))
#     answer_dict = {}
#     for three_bind_list in three_bind_lists:
#         answer_dict[tuple(three_bind_list)] = sum(three_bind_list)
#
#     sum_0_answer_unsort = map(list, dict(filter(lambda x: x[1] == 0, answer_dict.items())).keys())
#     sum_0_answer_sort = []
#     for item in sum_0_answer_unsort:
#         sorted_item = sorted(item)
#         if sorted_item in sum_0_answer_sort:
#             continue
#         sum_0_answer_sort.append(sorted_item)
#     return sum_0_answer_sort
#
#
# print(three_sum([-1, 0, 1, 2, -1, -4]))

def three_sum(nums):
    sorted_nums = sorted(nums)
    answer_list = []
    for left in range(len(sorted_nums) - 2):
        if left > 0 and sorted_nums[left] == sorted_nums[left - 1]:
            continue
        mid, right = left + 1, len(sorted_nums) - 1
        while mid < right:
            sum_num = sorted_nums[left] + sorted_nums[mid] + sorted_nums[right]
            if sum_num < 0:
                mid += 1
            elif sum_num > 0:
                right -= 1
            else:
                answer_list.append([sorted_nums[left], sorted_nums[mid], sorted_nums[right]])

                while mid < right and sorted_nums[mid] == sorted_nums[mid + 1]:
                    mid += 1
                while right > mid and sorted_nums[right] == sorted_nums[right - 1]:
                    right -= 1

                mid += 1
                right -= 1

    return answer_list


print(three_sum(
    [-1, 0, 1, 2, -1, -4]))
