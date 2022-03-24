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
    
    # Breadth First append. Values are filled layer by layer, horizontally
    def BF_append(self, data):
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

    # Binary Search Tree append. Valid only for data that can be compared numerically
    def BST_append(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            current = self.root
            parent = None
            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left
                    if current is None:
                        parent.left = node
                        break
                else:
                    current = current.right
                    if current is None:
                        parent.right = node
                        break
            self.size += 1

    # the pop process is different depending on how many child nodes the target has
    def BST_pop_node(self, data):
        if self.search(data):
            current = self.root
            if data == current.data:
                if current.left is None and current.right is None:
                    self.root = None
                elif current.left is None:
                    self.root = current.right
                elif current.right is None:
                    self.root = current.left
                else:
                    current = current.right
                    if current.left is None:
                        current.left = self.root.left
                        self.root = current
                    else:
                        while current.left is not None:
                            parent = current
                            current = current.left
                        current.left = self.root.left
                        current.right = parent
                        parent.left = None
                        self.root = current
            else:
                while True:
                    parent = current
                    if data < parent.data:
                        current = current.left
                        if data == current.data:
                            if current.left is None and current.right is None:
                                parent.left = None
                            elif current.left is None:
                                parent.left = current.right
                            elif current.right is None:
                                parent.left = current.left
                            else:
                                if current.left is None:
                                    current.left = parent.left
                                    parent = current
                                else:
                                    root = parent
                                    while current.left is not None:
                                        parent = current
                                        current = current.left
                                    current.right = parent.right
                                    parent.left = None
                                    root.right = current
                            break
                    else:
                        current = current.right
                        if data == current.data:
                            if current.left is None and current.right is None:
                                parent.right = None
                            elif current.left is None:
                                parent.right = current.right
                            elif current.right is None:
                                parent.right = current.left
                            else:
                                if current.left is None:
                                    current.left = parent.left
                                    parent = current
                                else:
                                    root = parent
                                    while current.left is not None:
                                        parent = current
                                        current = current.left
                                    current.right = parent.right
                                    parent.left = None
                                    root.right = current
                            break
                self.size -= 1
                return data
            
    def display(self):
        if self.root is not None:
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
    
    # Breadth First tree traversal
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

    # Breadth First tree search
    def search(self, data):
        if self.root is not None:
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
        
    # Binary Search Tree search (valid only where append operations are also BST) 
    def BST_search(self, data):
        if self.root is not None:
            current = self.root
            while current is not None:
                if current.data == data:
                    return True
                if data < current.data:
                    current = current.left
                else:
                    current = current.right
            return False
        
    # Full sub-tree display, using Breadth First search and traversal
    def display_subtree(self, data):
        if self.root is not None:
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

    # Full sub-tree delete, using Breadth First search and traversal            
    def pop_subtree(self, data):
        if self.root is not None:
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

    # it relies on Breadth First traversal
    def display_leaves(self):
        if self.root is not None:
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
    
    # it relies on Breadth First traversal
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
    
    # the furthest bottom-left node
    def min_node(self):
        if self.root is not None:
            node = self.root
            while node.left is not None:
                node = node.left
            return node.data

    # the furthest bottom-right node
    def max_node(self):
        if self.root is not None:
            node = self.root
            while node.right is not None:
                node = node.right
            return node.data

    # display the level value of a node
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

    # display the heigth of the tree
    def height(self):
        if self.root is not None:
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

    # display the width of the tree
    def width(self):
        if self.root is not None:
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
    
    # delete all the nodes of the whole tree
    def flush(self):
        self.root = None
        self.size = 0
