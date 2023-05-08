# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    # 년, 월, 일을 일수로 변환하는 함수
    def date_to_day(date_string):
        result = 0
        split_list = list(map(int, date_string.split('.')))
        result += (split_list[0] * 336) + ((split_list[1] - 1) * 28) + split_list[2]
        return result

    terms_dict = dict()
    for term in terms:
        [s_term, s_duration] = term.split(' ')
        terms_dict[s_term] = int(s_duration) * 28

    result = []
    today = date_to_day(today)
    for p_idx, privacy in enumerate(privacies):
        [p_day, p_term] = privacy.split(' ')
        p_day = date_to_day(p_day)
        if p_day + terms_dict[p_term] - 1 < today:
            result.append(p_idx + 1)
    return result