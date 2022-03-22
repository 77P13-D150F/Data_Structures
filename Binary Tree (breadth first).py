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
                queue.append(current.left)
                queue.append(current.right)
        self.size += 1
            
    def extract(self):
        list_nodes = []
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            list_nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return list_nodes

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

    def subtree(self, data):
        queue = deque([self.root])
        while len(queue) > 0:
            node = queue.popleft()
            if node.data != data:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                list_nodes = []
                queue = deque([node])
                while len(queue) > 0:
                    node = queue.popleft()
                    list_nodes.append(node.data)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                return list_nodes

    def leaves(self):
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
        return leaves
    
    def min_node(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def max_node(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data
