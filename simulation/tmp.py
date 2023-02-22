def solution(name):
    # A - 65 / Z - 90
    name_len = len(name)
    curr_string = ['A' for _ in range(len(name))]
    result = 0
    curr_pos = 0
    while True:
        if name == ''.join(curr_string):
            break
        left_pos, right_pos = curr_pos, curr_pos
        left_count, right_count = 0, 0
        while curr_string[right_pos] == name[right_pos]:
            if right_pos == name_len - 1:
                right_pos = 0
            else:
                right_pos += 1
            right_count += 1
        while curr_string[left_pos] == name[left_pos]:
            if left_pos == 0:
                left_pos = name_len - 1
            else:
                left_pos -= 1
            left_count += 1
        if right_pos <= left_pos:
            curr_pos = right_pos
            result += right_count
        else:
            curr_pos = left_pos
            result += left_count
        result += min(ord(name[curr_pos]) - 65, 90-ord(name[curr_pos])+1)
        curr_string[curr_pos] = name[curr_pos]
    return result

solution("JAN")