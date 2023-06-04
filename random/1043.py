# 거짓말 : https://www.acmicpc.net/problem/1043
# 지민이는 파티에서 가장 좋아하는 이야기를 함
# 진실이거나 MSG왕창이거나
# 되도록 과장해서 이야기하지만 거짓말쟁이로 알려지고 싶지 않음
# 일부 사람이 지민이가 하는 이야기의 진실을 알고 있음.

from sys import stdin

input = stdin.readline

n, m = map(int, input().split(' '))
checker = list(map(int, input().split(' ')))
checker = set(checker[1:])

party_list = []

for _ in range(m):
    party = list(map(int, input().split(' ')))
    party_list.append(set(party[1:]))

for _ in range(m):
    for party in party_list:
        if set.intersection(party, checker):
            checker = set.union(party, checker)

result = 0
for party in party_list:
    if set.intersection(party, checker):
        continue
    result += 1
print(result)
