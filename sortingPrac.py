# 수 정렬하기: https://www.acmicpc.net/problem/2750
import sys
import random

input = sys.stdin.readline

N = int(input())
N_list = []
for _ in range(N):
    N_list.append(int(input()))
N_len = len(N_list)


# bubble sort
# for level in range(N_len-2, -1, -1):
#     for target in range(level+1):
#         if N_list[target] > N_list[target+1]:
#             N_list[target], N_list[target+1] = N_list[target+1], N_list[target]
# for n in N_list:
#     print(n)

# selection sort
# for input_pos in range(N_len - 1):
#     min_val, min_pos = float('inf'), -1
#     for target in range(input_pos, N_len):
#         if N_list[target] < min_val:
#             min_val = N_list[target]
#             min_pos = target
#     N_list[min_pos], N_list[input_pos] = N_list[input_pos], N_list[min_pos]
#
# for n in N_list:
#     print(n)

# insertion sort
# def insert(insert_val, insert_pos, end_pos):
#     for target in range(end_pos, insert_pos, -1):
#         N_list[target], N_list[target - 1] = N_list[target - 1], N_list[target]
#     N_list[insert_pos] = insert_val
#
#
# for turn in range(1, N_len):
#     point = turn - 1
#     while point >= 0 and N_list[turn] < N_list[point]:
#         point -= 1
#     insert(N_list[turn], point + 1, turn)
#
# for n in N_list:
#     print(n)

# quick sort
def quick_sort(start, end):
    if start >= end:
        return
    pivot_idx = random.randint(start, end)
    N_list[pivot_idx], N_list[end] = N_list[end], N_list[pivot_idx]
    left, right = start, end - 1
    while True:
        while left <= right and N_list[left] <= N_list[end]:
            left += 1
        while left <= right and N_list[right] >= N_list[end]:
            right -= 1
        if left > right:
            break
        N_list[left], N_list[right] = N_list[right], N_list[left]
    N_list[left], N_list[end] = N_list[end], N_list[left]
    quick_sort(start, left - 1)
    quick_sort(left + 1, end)


# quick_sort(0, N_len - 1)

# merge sort
tmp_list = [0 for _ in range(N_len + 1)]


def merge_sort(start, end):
    if start + 1 == end:
        return
    # 절반으로 계속 나누기
    mid = (start + end) // 2
    merge_sort(start, mid)
    merge_sort(mid, end)

    left_point, right_point = start, mid
    for t in range(start, end):
        if left_point == mid:
            tmp_list[t] = N_list[right_point]
            right_point += 1
        elif right_point == end:
            tmp_list[t] = N_list[left_point]
            left_point += 1
        elif N_list[left_point] <= N_list[right_point]:
            tmp_list[t] = N_list[left_point]
            left_point += 1
        else:
            tmp_list[t] = N_list[right_point]
            right_point += 1
    for t in range(start, end):
        N_list[t] = tmp_list[t]


# merge_sort(0, N_len)

# heap sort
class Heap:
    def __init__(self):
        self.queue = [0]
        self.count = 0

    def heappush(self, val):
        self.queue.append(val)
        self.count += 1
        target_idx = self.count
        while target_idx > 1 and self.queue[target_idx] < self.queue[target_idx // 2]:
            self.queue[target_idx], self.queue[target_idx // 2] = self.queue[target_idx // 2], self.queue[target_idx]
            target_idx = target_idx // 2

    def heappop(self):
        if self.count == 0:
            return
        store = self.queue[1]
        self.queue[1], self.queue[self.count] = self.queue[self.count], self.queue[1]
        self.queue.pop()
        self.count -= 1

        if self.count <= 1:
            return store

        target_idx = 1
        while target_idx <= (self.count // 2):
            left_child = target_idx * 2
            right_child = (target_idx * 2) + 1
            tmp_max_idx = target_idx
            is_changed = False
            if left_child <= self.count and self.queue[left_child] < self.queue[tmp_max_idx]:
                is_changed = True
                tmp_max_idx = left_child
            if right_child <= self.count and self.queue[right_child] < self.queue[tmp_max_idx]:
                is_changed = True
                tmp_max_idx = right_child
            if not is_changed:
                break
            self.queue[target_idx], self.queue[tmp_max_idx] = self.queue[tmp_max_idx], self.queue[target_idx]
            target_idx = tmp_max_idx
        return store


heap = Heap()
for n in N_list:
    heap.heappush(n)

for _ in range(N_len):
    print(heap.heappop())

# for n in N_list:
#     print(n)
