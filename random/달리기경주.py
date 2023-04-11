# https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    player_to_rank_dict = dict()
    rank_to_player_dict = dict()
    for rank, player in enumerate(players):
        player_to_rank_dict[player] = rank
        rank_to_player_dict[rank] = player
    for call in callings:
        caller_rank = player_to_rank_dict[call]
        target_rank = caller_rank - 1
        target = rank_to_player_dict[target_rank]
        player_to_rank_dict[call] -= 1
        player_to_rank_dict[target] += 1
        rank_to_player_dict[caller_rank] = target
        rank_to_player_dict[target_rank] = call
    result = [(p, r) for p, r in player_to_rank_dict.items()]
    result.sort(key=lambda x:x[1])
    return [p for p, r in result]