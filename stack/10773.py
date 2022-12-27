# 재민이는 동아리 회식을 위해 장부를 관리하고 있다
# 재현이는 재민이를 도와 돈을 관리한다.
# 재현이가 잘못된 수를 부를 때 마다 0을 외쳐 재민이가 쓴 수를 지우게 한다
# 재민이는 이 수를 모두 받아 적고 그 수의 합을 알고 싶어 한다.

from sys import stdin
s_input = stdin.readline

result = []

k = int(s_input())
for _ in range(k):
    num = int(s_input())
    if num == 0:
        if result:
            result.pop()
    else:
        result.append(num)
print(sum(result))
