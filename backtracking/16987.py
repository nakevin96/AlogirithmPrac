n = int(input())
durability_list = [0 for _ in range(n)]
weight_list = [0 for _ in range(n)]

for i in range(n):
    durability_list[i], weight_list[i] = map(int, input().split(" "))

result = 0


def sol(idx, eggs):
    global result
    if idx == n:
        cnt = 0
        for i in range(n):
            if eggs[i] <= 0:
                cnt += 1
        if cnt > result:
            result = cnt
        return
    if eggs[idx] > 0:
        for i in range(n):
            flag = False
            if eggs[i] > 0 and i != idx:
                flag = True
                tmp = eggs[:]
                tmp[i] -= weight_list[idx]
                tmp[idx] -= weight_list[i]
                sol(idx + 1, tmp)
            if not flag:
                sol(idx + 1, eggs)
    else:
        sol(idx + 1, eggs)


sol(0, s)
print(result)
