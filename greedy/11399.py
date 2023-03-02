N = int(input())
time_list = list(map(int, input().split(' ')))
time_list.sort()
n_count = N
result = 0
for time in time_list:
    result += (n_count * time)
    n_count -= 1
print(result)
