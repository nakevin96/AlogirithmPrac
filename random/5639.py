# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# root_node = None
#
#
# class BinaryTreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#
#     def get_val(self):
#         return self.val
#
#     def set_val(self, val):
#         self.val = val
#
#     def get_left(self):
#         return self.left
#
#     def set_left(self, left_node):
#         self.left = left_node
#
#     def get_right(self):
#         return self.right
#
#     def set_right(self, right_node):
#         self.right = right_node
#
#
# while True:
#     try:
#         input_val = int(input().rstrip())
#         checker = root_node
#         curr_node = BinaryTreeNode(input_val)
#         if not checker:
#             root_node = curr_node
#             continue
#
#         while True:
#             checker_val = checker.get_val()
#             if checker_val > input_val:
#                 checker_left = checker.get_left()
#                 if not checker_left:
#                     checker.set_left(curr_node)
#                     break
#                 checker = checker_left
#             else:
#                 checker_right = checker.get_right()
#                 if not checker_right:
#                     checker.set_right(curr_node)
#                     break
#                 checker = checker_right
#
#     except:
#         break
#
#
# def search(s_node):
#     if s_node.get_left():
#         search(s_node.get_left())
#     if s_node.get_right():
#         search(s_node.get_right())
#     print(s_node.get_val())
#
#
# search(root_node)


import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

root_node = None


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


while True:
    try:
        input_val = int(input().rstrip())
        checker = root_node
        curr_node = BinaryTreeNode(input_val)
        if not checker:
            root_node = curr_node
            continue

        while True:
            if checker.val > input_val:
                if not checker.left:
                    checker.left = curr_node
                    break
                checker = checker.left
            else:
                if not checker.right:
                    checker.right = curr_node
                    break
                checker = checker.right

    except:
        break


def search(s_node):
    if s_node.left:
        search(s_node.left)
    if s_node.right:
        search(s_node.right)
    print(s_node.val)


search(root_node)


# import sys
#
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline
#
# root_node = None
#
# tree_dict = dict()
#
# while True:
#     try:
#         input_val = int(input().rstrip())
#         checker = 's'
#
#         if checker not in tree_dict:
#             tree_dict[checker] = input_val
#             continue
#
#         while True:
#             if tree_dict[checker] > input_val:
#                 if checker + 'l' not in tree_dict:
#                     tree_dict[checker + 'l'] = input_val
#                     break
#                 checker = checker + 'l'
#             else:
#                 if checker + 'r' not in tree_dict:
#                     tree_dict[checker + 'r'] = input_val
#                     break
#                 checker = checker + 'r'
#
#     except:
#         break
#
# def search(check_string):
#     if check_string + 'l' in tree_dict:
#         search(check_string + 'l')
#     if check_string + 'r' in tree_dict:
#         search(check_string + 'r')
#     if check_string in tree_dict:
#         print(tree_dict[check_string])
#
#
# search('s')
