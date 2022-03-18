#/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
    
    def __repr__(self):
        return self.data


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.previous = node
            self.head = self.head.previous
        self.size += 1
            
    def dequeue(self):
        if self.head is not None:
            data = self.tail
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return data
        else:
            return None

    def flush(self):
        self.head = None
        self.tail = None
        self.size = 0
