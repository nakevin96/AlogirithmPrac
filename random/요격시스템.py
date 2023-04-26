def solution(targets):
    targets.sort(key=lambda x: x[1])
    count = 0
    curr_target_idx = 0
    while curr_target_idx < len(targets):
        count += 1
        end_coord = targets[curr_target_idx][1]
        while curr_target_idx < len(targets) and end_coord  > targets[curr_target_idx][0]:
            curr_target_idx += 1
    return count