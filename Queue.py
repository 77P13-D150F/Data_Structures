#/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
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
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.head is not None:
            data = self.head
            self.head = self.head.next
            self.size -= 1
            return data
        else:
            return None
        
    def flush(self):
        self.head = None
        self.tail = None
        self.size = 0
