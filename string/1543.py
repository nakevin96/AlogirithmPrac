# 문자열 검색: https://www.acmicpc.net/problem/1543

document = input()
target_word = input()
checked = [False for _ in range(len(document))]
result = 0
for word_start in range(len(document)-len(target_word)+1):
    is_match = True
    for check_adder in range(len(target_word)):
        if checked[word_start+check_adder] or (target_word[check_adder] != document[word_start+check_adder]):
            is_match = False
            break

    if is_match:
        for check_adder in range(len(target_word)):
            checked[word_start+check_adder] = True
        result += 1

print(result)


