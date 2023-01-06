# A: 65  Z:  90
def solution(name):
    def get_alpha_move(curr_alpha):
        alpa_num = ord(curr_alpha)
        diff = alpa_num - 65
        return min(diff, 26 - diff)

    def get_next_right(r):
        return 0 if r == name_len-1 else r+1

    def get_next_left(l):
        return name_len-1 if l==0 else l-1

    def get_next_move(curr_idx):
        right_check = left_check = 0
        right_tmp = left_tmp = curr_idx
        while name[get_next_right(right_tmp)] == 'A' and check[get_next_right(right_tmp)] == 0:
            check[right_tmp] = 1
            right_tmp = get_next_right(right_tmp)
            right_check += 1

        while name[get_next_left(left_tmp)] == 'A' and check[get_next_left(left_tmp)] == 0:
            check[left_tmp] = 1
            left_tmp = get_next_left(left_tmp)
            left_check += 1

        if left_check <= right_check:
            return left_tmp, left_check
        else:
            return right_tmp, right_check

    name_len = len(name)
    check = [0 for _ in range(len(name))]

    idx = 0
    result = 0
    while 0 in check:
        result += get_alpha_move(name[idx])
        check[idx] = 1
        next_idx, next_val = get_next_move(idx)
        result += next_val
        idx = next_idx
    return result


print(solution("AAAA"))
