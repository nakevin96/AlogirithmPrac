def solve3():
    import sys
    N, K = map(int, sys.stdin.readline().split())
    word_list = [sys.stdin.readline().strip() for _ in range(N)]
    alph = [0] * 26

    def dfs(idx, cnt):
        nonlocal result
        if K - 5 == cnt:
            read_cnt = 0
            for word in word_list:
                is_read = True
                for w in word:
                    if alph[ord(w) - ord('a')] == 0:
                        is_read = False
                        break
                if is_read:
                    read_cnt += 1
            result = max(result, read_cnt)
            return

        for i in range(idx, 26):
            if alph[i] == 0:
                alph[i] = 1
                dfs(i + 1, cnt + 1)
                alph[i] = 0

    if K < 5:
        print(0)
    else:
        for char in ('a', 'c', 'i', 'n', 't'):
            alph[ord(char) - ord('a')] = 1

        result = 0
        dfs(0, 0)
        print(result)


solve3()
