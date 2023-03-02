import sys

input = sys.stdin.readline

N = int(input())
meeting_list = []
for _ in range(N):
    s_time, e_time = map(int, input().split(" "))
    meeting_list.append((s_time, e_time))

meeting_list.sort(key=lambda x: (x[1], x[0]))
cnt = 1
end_t = meeting_list[0][1]

for mi in range(1, N):
    if meeting_list[mi][0] < end_t:
        continue
    cnt += 1
    end_t = meeting_list[mi][1]
print(cnt)
