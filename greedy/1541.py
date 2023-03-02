expression = list(input())

result = []
num_str = ''
is_occur = False
for ex in expression:
    if ex == '+':
        result.append(int(num_str))
        if is_occur:
            result.append('-')
        else:
            result.append('+')
        num_str = ''

    elif ex == '-':
        is_occur = True
        result.append(int(num_str))
        result.append('-')
        num_str = ''

    else:
        num_str += ex

result.append(int(num_str))
sum_val = 0
flag = True
for r in result:
    if r == '+':
        flag = True
    elif r == '-':
        flag = False
    else:
        if flag:
            sum_val += r
        else:
            sum_val -= r
print(sum_val)


