from collections import deque

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

        
def isOperator(c):
    if c in '+-*/':
        return True
    return False


def postorder_build(expr):
    stack = []
    for c in expr:
        if not isOperator(c):
            node = Node(int(c))
            stack.append(node)
        else:
            node = Node(c)
            node.right = stack.pop()
            node.left = stack.pop()
            stack.append(node)
    return stack.pop()


def inorder_display(tree, nodes=[]):
    if tree is not None:
        inorder_display(tree.left, nodes)
        nodes.append(tree.data)
        inorder_display(tree.right, nodes)
        return nodes

def BF_display(tree):
    nodes = []
    queue = deque([tree])
    while len(queue) > 0:
        node = queue.popleft()
        nodes.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return nodes

def solve(node):
    if node.data == '+':
        return solve(node.left) + solve(node.right)
    if node.data == '-':
        return solve(node.left) - solve(node.right)
    if node.data == '*':
        return solve(node.left) * solve(node.right)
    if node.data == '/':
        return solve(node.left) / solve(node.right)
    else:
        return node.data
    
expr = '4 5 + 5 3 - *'.split(' ') # the expression must be in postorder notation
