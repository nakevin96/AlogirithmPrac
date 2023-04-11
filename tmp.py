# def solution(plans):
#     class Heap:
#         def __init__(self):
#             self.queue = [0]
#             self.size = 0
#
#         def heaptop(self):
#             if self.size == 0:
#                 return []
#             else:
#                 return self.queue[1]
#
#         def haveToChange(self, a, b):
#             # False a가 더 먼저 처리해야 해서 안바꿔도 됌 True 바꿔야함
#             if self.queue[a][1] < self.queue[b][1]:
#                 return False
#             elif self.queue[a][1] == self.queue[b][1]:
#                 # 시작 시간이 동일한 상황 => 새작업 먼저
#                 if self.queue[a][4] == 1 and self.queue[b][4] == 0:
#                     return False
#                 elif self.queue[a][4] == 0 and self.queue[b][4] == 1:
#                     return True
#                 else:
#                     # 시작시간 동일하며 둘 다 새작업인 경우는 없으니 여기서는 둘 다 남은 작업
#                     # 이 경우 최근 멈춘 작업부터 (카운트가 클 수록 최근 작업)
#                     if self.queue[a][3] > self.queue[b][3]:
#                         return False
#                     else:
#                         return True
#             else:
#                 return True
#
#         def heappush(self, item):
#             # item = [라벨, 시작 시간, 남은 시간, 카운트, 새작업여부]
#             self.queue.append(item)
#             self.size += 1
#             child = self.size
#             while True:
#                 if child == 1:
#                     break
#                 parent = child // 2
#                 if self.haveToChange(parent, child):
#                     self.queue[parent], self.queue[child] = self.queue[child], self.queue[parent]
#                     child = parent
#                 else:
#                     break
#
#         def heappop(self):
#             if self.size == 0:
#                 return
#             self.queue[1], self.queue[self.size] = self.queue[self.size], self.queue[1]
#             returnVal = self.queue.pop()
#             self.size -= 1
#
#             parent_pos = 1
#             while True:
#                 left_pos, right_pos = parent_pos * 2, parent_pos * 2 + 1
#                 if left_pos > self.size:
#                     break
#                 compare_pos = left_pos
#                 if right_pos <= self.size and self.haveToChange(left_pos, right_pos):
#                     compare_pos = right_pos
#                 if self.haveToChange(parent_pos, compare_pos):
#                     self.queue[parent_pos], self.queue[compare_pos] = self.queue[compare_pos], self.queue[parent_pos]
#                 else:
#                     break
#             return returnVal
#
#     heap = Heap()
#     for p in plans:
#         h, m = map(int, p[1].split(':'))
#         heap.heappush([p[0], h * 60 + m, int(p[2]), 0, 1])
#
#     result = []
#     count = 0
#     while heap.size > 0:
#         # label, startTime, remainTime, newest, newJob
#         count += 1
#         curr_work = heap.heappop()
#         if heap.size == 0:
#             result.append(curr_work[0])
#         else:
#             next_work = heap.heaptop()
#             if curr_work[1] + curr_work[2] <= next_work[1]:
#                 result.append(curr_work[0])
#             else:
#                 heap.heappush([curr_work[0], next_work[0], ])
#     return result

def solution(plans):
    new_works = []
    old_works = []
    result = []
    curr_time = float('INF')
    for p in plans:
        h, m = map(int, p[1].split(':'))
        new_works.append([p[0], h * 60 + m, int(p[2])])
        curr_time = min(curr_time, h*60 + m)
    new_works.sort(key=lambda x: -x[1])

    while new_works:
        next_new = new_works.pop()
        if next_new[1] > curr_time:
            while old_works:
                next_old = old_works.pop()
                if next_old[2] <= next_new[1] - curr_time:
                    result.append(next_old[0])
                    curr_time += next_old[2]
                else:
                    old_works.append([next_old[0], curr_time, next_old[2] - (next_new[1] - curr_time)])
                    curr_time = next_new[1]
                    break
        future_work = None
        if new_works:
            future_work = new_works[-1]
        if future_work == None:
            result.append(next_new[0])
            curr_time = next_new[1]
        else:
            if next_new[1] + next_new[2] <= future_work[1]:
                result.append(next_new[0])
                curr_time = next_new[1] + next_new[2]
            else:
                old_works.append([next_new[0], future_work[1], next_new[2] - (future_work[1] - next_new[1])])
                curr_time = future_work[1]

    while old_works:
        result.append(old_works.pop()[0])
    return result


print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]))
