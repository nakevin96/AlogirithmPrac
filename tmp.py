def sol(pattern):
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[j] != pattern[i]:
            j = table[j - 1]
        if pattern[j] == pattern[i]:
            j += 1
            table[i] = j

    print(table)
