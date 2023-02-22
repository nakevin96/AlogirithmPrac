truck_num, bridge_len, limit_weight = map(int, input().split(" "))
truck_weights = list(map(int, input().split(" ")))
if truck_num == 1:
    print(bridge_len + 1)
else:
    curr_idx = 1
    weight_idx = 0
    time_weight_list = [0 for _ in range((bridge_len + 1) * truck_num + 1)]
    while weight_idx < truck_num:
        if time_weight_list[curr_idx] + truck_weights[weight_idx] <= limit_weight:
            for check_idx in range(curr_idx, curr_idx + bridge_len):
                time_weight_list[check_idx] += truck_weights[weight_idx]
            weight_idx += 1
            curr_idx += 1
        else:
            while time_weight_list[curr_idx] + truck_weights[weight_idx] > limit_weight:
                curr_idx += 1
    while time_weight_list[curr_idx] > 0:
        curr_idx += 1
    print(curr_idx)
