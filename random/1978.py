N = int(input())
N_list = list(map(int, input().split(' ')))


def is_prime(target_num):
    if target_num <= 1:
        return False
    for i in range(2, int(target_num ** (0.5)) + 1):
        if target_num % i == 0:
            return False
    return True


result = 0
for n in N_list:
    if is_prime(n):
        result += 1
print(result)
