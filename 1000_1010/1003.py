fibocount = []
fibocount.append([1, 0])
fibocount.append([0, 1])
for i in range(39):
    fibocount.append([int(0), int(0)])


def fibonacci(num):
    global fibocount
    num = int(num)
    if num == 0:
        return [1, 0]
    elif num == 1:
        return [0, 1]
    else:
        if fibocount[num][0] != 0:
            return fibocount[num]
        else:
            tmp_a = fibonacci(num-1)
            tmp_b = fibonacci(num-2)
            fibocount[num][0] = tmp_a[0]+tmp_b[0]
            fibocount[num][1] = tmp_a[1]+tmp_b[1]
            return fibocount[num]


test_num = input()
for i in range(int(test_num)):
    test = int(input())
    fibonacci(test)
    print("{0} {1}".format(fibocount[test][0], fibocount[test][1]))
