# 최대 공약수 하나 빼기 : https://www.acmicpc.net/problem/14476
N = int(input())
N_list = list(map(int, input().split(' ')))


def calculate_gcd(num_a, num_b):
    while num_a % num_b != 0:
        num_a, num_b = num_b, num_a % num_b
    return num_b


left_to_right_gcd_store = [0 for _ in range(N)]
right_to_left_gcd_store = [0 for _ in range(N)]
left_to_right_gcd_store[0] = N_list[0]
right_to_left_gcd_store[-1] = N_list[-1]

for num_idx in range(1, N):
    left_to_right_gcd_store[num_idx] = calculate_gcd(left_to_right_gcd_store[num_idx - 1], N_list[num_idx])
for num_idx in range(N - 2, -1, -1):
    right_to_left_gcd_store[num_idx] = calculate_gcd(N_list[num_idx], right_to_left_gcd_store[num_idx + 1])

max_gcd_result = -1
selected_num = -1

# 맨 앞 뺏을 때
if N_list[0] % right_to_left_gcd_store[1] != 0:
    if max_gcd_result < right_to_left_gcd_store[1]:
        max_gcd_result = right_to_left_gcd_store[1]
        selected_num = N_list[0]

# 맨 뒤 뺏을 때
if N_list[-1] % left_to_right_gcd_store[-2] != 0:
    if max_gcd_result < left_to_right_gcd_store[-2]:
        max_gcd_result = left_to_right_gcd_store[-2]
        selected_num = N_list[-1]

# 가운데 뺏을 때
for target_num in range(1, N-1):
    mid_gcd = calculate_gcd(left_to_right_gcd_store[target_num-1], right_to_left_gcd_store[target_num+1])
    if N_list[target_num] % mid_gcd != 0:
        if max_gcd_result < mid_gcd:
            max_gcd_result = mid_gcd
            selected_num = N_list[target_num]

if max_gcd_result <= 1:
    print(-1)
else:
    print(f'{max_gcd_result} {selected_num}')
