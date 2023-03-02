N, M = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

result = []
ai, bi = 0, 0
while ai < N and bi < M:
    if A[ai] <= B[bi]:
        result.append(str(A[ai]))
        ai += 1
    else:
        result.append(str(B[bi]))
        bi += 1

while ai < N:
    result.append(str(A[ai]))
    ai += 1

while bi < M:
    result.append(str(B[bi]))
    bi += 1

print(' '.join(result))
