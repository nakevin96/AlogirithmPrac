# 생태학: https://www.acmicpc.net/problem/4358
from sys import stdin

input = stdin.readline
tree_count = dict()
total = 0
while True:
    tree_name = input().rstrip()
    if not tree_name:
        break
    total += 1
    if tree_name in tree_count:
        tree_count[tree_name] += 1
    else:
        tree_count[tree_name] = 1

tree_list = sorted(list(tree_count.keys()))
for tree in tree_list:
    print('%s %.4f' % (tree, tree_count[tree] / total * 100))
