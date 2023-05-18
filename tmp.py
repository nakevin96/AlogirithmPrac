def is_divided(target, mod):
    return target % mod == 0


for i in range(1, 10):
    print(f'{i} : {is_divided(111111 * i, 7)}, result: {(111111 * i) // 7}')

print(f'{is_divided(15, 7)}, result: {(15) // 7}')
