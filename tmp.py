def solution(K, user_scores):
    # lank page가 바뀌는 수
    user_score_dict = {}
    result = set()

    for i in range(len(user_scores)):
        user, score = user_scores[i].split(' ')
        # 한 user의 나중에 시도한 점수가 낮다면 갱신해주지 않음
        if user in user_score_dict and user_score_dict[user][0] >= int(score):
            continue
        else:
            user_score_dict[user] = (int(score), i)

        lankpage = [(key, val[0], val[1]) for key, val in user_score_dict.items()]
        # 점수와 먼저 나온 이름 순으로 정렬을 해줌
        sorted_lankpage = sorted(lankpage, key=lambda x:(-x[1], x[2]))[:K]
        # 정렬된 리시트에서 이름만 뽑아줌
        sorted_lank_user = [x[0] for x in sorted_lankpage]
        # 이름을 set()에 넣어서 중복을 없애줌
        result.add(tuple(sorted_lank_user))

    return len(result)

print(solution(3, ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"])) #4
print(solution(3, ["alex111 100", "cheries2 200", "alex111 200", "cheries2 150", "coco 50", "coco 200"])) #3
print(solution(2, ["cheries2 200", "alex111 100", "coco 150", "puyo 120"])) #3
print(solution(1, ['a 1', 'b 2', 'c 3', 'd 4'])) # 4
print(solution(1, ['a 10', 'a 9', 'a 8', 'a 7', 'a 6', 'a 5', 'b 100'])) # 2
print(solution(2, ['a 100', 'b 100', 'c 100', 'd 100', 'a 200', 'a 300', 'a 400', 'd 600'])) # 3
print(solution(5, ['a 100', 'c 200', 'd 150'])) # 3

'''
테스트 1
입력값 〉
3, ["alex111 100", "cheries2 200", "coco 150", "luna 100", "alex111 120", "coco 300", "cheries2 110"]
기댓값 〉
4
실행 결과 〉
테스트를 통과하였습니다.
출력 〉
3 ['alex111 100', 'cheries2 200', 'coco 150', 'luna 100', 'alex111 120', 'coco 300', 'cheries2 110']
테스트 2
입력값 〉
3, ["alex111 100", "cheries2 200", "alex111 200", "cheries2 150", "coco 50", "coco 200"]
기댓값 〉
3
실행 결과 〉
테스트를 통과하였습니다.
출력 〉
3 ['alex111 100', 'cheries2 200', 'alex111 200', 'cheries2 150', 'coco 50', 'coco 200']
테스트 3
입력값 〉
2, ["cheries2 200", "alex111 100", "coco 150", "puyo 120"]
기댓값 〉
3
실행 결과 〉
테스트를 통과하였습니다.
출력 〉
2 ['cheries2 200', 'alex111 100', 'coco 150', 'puyo 120']
'''