from sys import stdin

curl_list = list(stdin.readline().rstrip())
stack = []

result = 0
before = "("
for c in curl_list:
    if c == "(":
        stack.append("(")
        before = "("
    elif c == ")":
        if before == "(":
            stack.pop()
            result += len(stack)
            before = ")"

        else:
            stack.pop()
            result += 1
            before = ")"
print(result)
