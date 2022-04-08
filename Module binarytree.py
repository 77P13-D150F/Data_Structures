from binarytree import Node
from binarytree import tree


        
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


def solve(node):
    if node.value == '+':
        return solve(node.left) + solve(node.right)
    if node.value == '-':
        return solve(node.left) - solve(node.right)
    if node.value == '*':
        return solve(node.left) * solve(node.right)
    if node.value == '/':
        return solve(node.left) / solve(node.right)
    else:
        return node.value
    
expr = '4 5 + 5 3 - *'.split(' ') # postorder notation
tree = postorder_build(expr)
tree = tree.clone()
print(tree)
print(solve(tree))
