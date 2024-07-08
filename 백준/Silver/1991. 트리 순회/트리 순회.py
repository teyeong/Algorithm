class Node:
    def __init__(self, item):
        self.item = item
        self.left = self.right = None

def preorder(node):
    if node:
        print(node.item, end="")
        preorder(node.left)
        preorder(node.right)
    
def inorder(node):
    if node:
        inorder(node.left)
        print(node.item, end="")
        inorder(node.right)
        
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.item, end="")

N = int(input())
tree = {}

for i in range(N):
    a, b, c = input().split()
    
    if a not in tree:
        tree[a] = Node(a)
        if i == 0:
            root = tree[a]
    if b != '.':
        tree[b] = Node(b)
        tree[a].left = tree[b]
    if c != '.':
        tree[c] = Node(c)
        tree[a].right = tree[c]

preorder(root)
print()
inorder(root)
print()
postorder(root)