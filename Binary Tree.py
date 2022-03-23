#/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import deque


class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
    
    def __repr__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            queue = deque([self.root])
            while True:
                current = queue.popleft()
                if current.left is None:
                    current.left = node
                    break
                if current.right is None:
                    current.right = node
                    break
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        self.size += 1

    # valid only for data that can be compared numerically
    def BST_append(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            queue = deque([self.root])
            while len(queue) > 0:
                current = queue.popleft()
                if (current.left is None) and (node.data < current.data):
                    current.left = node
                    break
                if (current.right is None) and (node.data > current.data):
                    current.right = node
                    break
                if current.left and node.data < current.data:
                    queue.append(current.left)
                if current.right and node.data > current.data:
                    queue.append(current.right)
        self.size += 1
            
    def display(self):
        print(f'In-order (Depth first): {self.inorder(self.root)}')
        print(f'Pre-order (Depth first): {self.preorder(self.root)}')
        print(f'Post-order (Depth first): {self.postorder(self.root)}')
        print(f'Breadth first: {self.breadth_first()}')
    
    # child left -> parent -> child right
    def inorder(self, node, results=[]):
        if node is None:
            return
        self.inorder(node.left, results)
        results.append(node.data)
        self.inorder(node.right, results)
        return results
    
    # parent -> child left -> child right 
    def preorder(self, node, results=[]):
        if node is None:
            return
        results.append(node.data)
        self.preorder(node.left, results)
        self.preorder(node.right, results)
        return results
    
    # child left -> child right -> parent
    def postorder(self, node, results=[]):
        if node is None:
            return
        self.postorder(node.left, results)
        self.postorder(node.right, results)
        results.append(node.data)
        return results
    
    # breadth first
    def breadth_first(self):
        nodes = []
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return nodes

    def search(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.data == data:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False

    def display_subtree(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.data != data:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                nodes = []
                queue = deque([node])
                while len(queue) > 0:
                    node = queue.popleft()
                    nodes.append(node.data)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                print(nodes)

    def pop_subtree(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.left.data == data:
                subtree_root = node.left
                node.left = None
                break
            if node.right.data == data:
                subtree_root = node.right
                node.right = None
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        queue = deque([subtree_root])
        nodes = []
        while len(queue) > 0:
            node = queue.popleft()
            nodes.append(node.data)
            self.size -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)   
        return nodes

    def display_leaves(self):
        leaves = []
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if (node.left is None) and (node.right is None):
                leaves.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print(leaves)
    
    def pop_leaf(self, data):
        if self.search(data):
            queue = deque([self.root])
            while len(queue) > 0:
                node = queue.popleft()
                if node.left.data == data and (node.left.left is None) and (node.left.right is None):
                    leaf = node.left.data
                    node.left = None
                    self.size -= 1
                    return leaf
                if node.right.data == data and (node.right.left is None) and (node.right.right is None):
                    leaf = node.right.data
                    node.right = None
                    self.size -= 1
                    return leaf
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        else:
            return None
        
    def min_node(self):
        node = self.root
        while node.left is not None:
            node = node.left
        return node.data

    def max_node(self):
        node = self.root
        while node.right is not None:
            node = node.right
        return node.data

    def level_node(self, data):
        if self.search(data):
            queue = deque([self.root])
            depth = 0
            c = 0
            while len(queue) > 0:
                layer = 2 ** depth
                node = queue.popleft()
                if data == node.data:
                    return depth
                c += 1
                queue.append(node.left)
                queue.append(node.right)
                if c == layer:
                    depth += 1
                    c = 0
        else:
            return None

    def height(self):
        queue = deque([self.root])
        depth = 0
        c = 0
        heights = [] 
        while len(queue) > 0:
            layer = 2 ** depth
            node = queue.popleft()
            heights.append(depth)
            c += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if c == layer:
                depth += 1
                c = 0
        return max(heights)

    def width(self):
        queue = deque([self.root])
        depth = 0
        c = 0
        width = []
        while len(queue) > 0:
            layer = 2 ** depth
            node = queue.popleft()
            c += 1
            width.append(c)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if c == layer:
                depth += 1
                c = 0
        return max(width)
    
    def flush(self):
        self.root = None
        self.size = 0
