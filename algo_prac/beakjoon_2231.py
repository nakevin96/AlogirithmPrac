def answer(number):
    sub = len(number) * 9
    number = int(number)

    for num in range(number - sub, number):
        result = num
        tmp = num
        while tmp:
            result += tmp % 10
            tmp = tmp // 10
        if result == number:
            return num

    return 0


input_num = input()
print(answer(input_num))
