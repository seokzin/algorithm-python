n = int(input())

tree = {}

for _ in range(n):
  root, l, r = input().split()
  tree[root] = [l, r]


def preorder(root):
  if root != '.':
    print(root, end='')  # root
    preorder(tree[root][0])  # l
    preorder(tree[root][1])  # r


def inorder(root):
  if root != '.':
    inorder(tree[root][0])  # l
    print(root, end='')  # root
    inorder(tree[root][1])  # r


def postorder(root):
  if root != '.':
    postorder(tree[root][0])  # l
    postorder(tree[root][1])  # r
    print(root, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')


# 트리 입력 받는 법? - 객체? 딕셔너리?로 받음으로써 알파벳 키값으로 값 접근이 편한 장점?
# 파이썬의 딕셔너리는 객체의 다른 말인가?
# 트리 탐색은 좌 우를 묶음으로 생각하여 하나씩 재귀 한다고 생각하면 좋다.