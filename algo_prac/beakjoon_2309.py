# 아홉 난쟁이의 키가 주어졌을 때
# 모든 난쟁이 키의 합이 100임을 기억하는 백설공주가 난쟁이를 골라내는 방법
# 입력 100을 넘지 않는 수 9개
def answer(input_list):
    height_sum = sum(input_list)

    for i in input_list:
        for j in input_list[input_list.index(i) + 1:]:
            if height_sum - i - j == 100:
                input_list.remove(i)
                input_list.remove(j)
                return sorted(input_list)


input_height = [20, 7, 23, 19, 10, 15, 25, 8, 13]
print(answer(input_height))
