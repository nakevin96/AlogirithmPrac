import math

# 계절 별 과일을 저장하는 딕셔너리
SEASONAL_FRUITS = {
    '봄': ['딸기', '수박'],
    '여름': ['딸기', '수박'],
    '가을': ['사과', '배'],
    '겨울': ['사과', '배']
}

# 해당 일자에 몇 번째 IDX에 위치한 과일을 공급할 것인지 저장해 둔 딕셔너리
DAY_FRUITS_IDX = {
    1: 0,
    3: 1,
    5: 0,
    7: 1,
}

# 과일이 한 사람당 몇 개 제공되는지 저장해둔 딕셔너리
FRUITS_PER_PERSON_COUNT = {
    '딸기': 5,
    '수박': 0.1,
    '사과': 1,
    '배': 0.5,
}


def get_season(month):
    if 3 <= month <= 5:
        return '봄'
    elif 6 <= month <= 8:
        return '여름'
    elif 9 <= month <= 11:
        return '가을'
    else:
        return '겨울'


def get_fruit_purchase_requisition(purchase_month=3, total_person=70):
    season = get_season(purchase_month)

    with open('Fruit_quiz_ChoiYoonSeok_order.txt', 'w', encoding='utf-8') as f:
        f.write(f'{purchase_month}월 디저트 구매 내역서(총 {total_person}명)\n\n')

        for day in range(1, 31):
            if day % 10 in DAY_FRUITS_IDX:
                today_fruit_idx = DAY_FRUITS_IDX[day % 10]
                today_fruit = SEASONAL_FRUITS[season][today_fruit_idx]
                total_fruit_count = math.ceil(total_person * FRUITS_PER_PERSON_COUNT[today_fruit])
                f.write(f'{purchase_month}월 {day}일: {today_fruit} {total_fruit_count}개\n')
            else:
                f.write(f'{purchase_month}월 {day}일: -\n')


if __name__ == '__main__':
    get_fruit_purchase_requisition()
