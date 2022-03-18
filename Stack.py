#/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def peek(self):
        print(self.top)
        
    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is not None:
            data = self.top
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            return None
        
    def clear(self):
        self.top = None
        self.size = 0
