# N = int(input())
# n_list = list(map(int, input().split(' ')))
# result = 0
# for n in n_list:
#     if n <= 1:
#         continue
#     is_prime = True
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             is_prime = False
#         i += 1
#     if is_prime:
#         result += 1
# print(result)
n = int(input())
n_list = list(map(int, input().split(' ')))
max_val = max(n_list)
prime = [0, 0]
prime.extend([1 for _ in range(max_val - 1)])
for i in range(2, (max_val // 2) + 1):
    for check in range(i + i, max_val + 1, i):
        prime[check] = 0

result = 0
for number in n_list:
    result += prime[number]
print(result)
