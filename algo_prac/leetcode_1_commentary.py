# 이 문제는 매우 쉽지만 최적화할 수 있는 여러 방법이 숨어 있어서 코드 인터뷰시 높은 빈도로 출제된다.

# 가장 비효율 적인 방식 (Brute force)
from typing import List


def two_sum1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값이 존재하는지 확인하는 방식으로 구성

def two_sum2(nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + i + 1]


# 첫 수를 뺀 결과 키 조회

def two_sum3(nums: List[int], target: int) -> List[int]:
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]
