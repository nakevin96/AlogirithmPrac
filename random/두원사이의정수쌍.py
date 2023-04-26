def solution(r1, r2):
    y_point1, y_point2 = r1, r2
    result = 0
    for x in range(r2):
        while y_point1 - 1 > 0 and x ** 2 + (y_point1 - 1) ** 2 >= r1 ** 2:
            y_point1 -= 1
        while x ** 2 + y_point2 ** 2 > r2 ** 2:
            y_point2 -= 1

        result += (y_point2 - y_point1) + 1
    return result * 4