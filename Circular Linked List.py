#/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def push_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            self.head.next = self.tail.previous = node
            self.head.previous= self.tail.next = node
        else:
            node.previous = self.tail
            self.tail.next = self.head.previous = node
            node.next = self.head
            self.tail = self.tail.next
        self.size += 1

    def push_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            self.head.next = self.tail.previous = node
            self.head.previous= self.tail.next = node
        else:
            node.next = self.head
            self.head.previous = self.tail.next = node
            node.previous = self.tail
            self.head = self.head.previous
        self.size += 1
    
    def rotate(self, n=0):
        current = self.head
        if n > 0:
            for i in range(n):
                current = current.next
        elif n < 0:
            for i in range(-1 * n):
                current = current.previous
        else:
            pass
        self.head = current
        self.tail = self.head.next
        self.tail.previous = self.head
    
    def reverse(self):
        previous_node = self.head.previous
        current = self.head
        next_node = self.head.next
        self.tail = current
        for i in range(self.size):
            next_node = current.next
            current.next = previous_node
            current.previous = next_node
            previous_node = current
            current = next_node
        self.head = previous_node
        
    def display(self, debug=False):
        if self.head is not None:
            current = self.head
            for i in range(self.size):
                if debug:
                    print(f'({current.previous} <--) {current} (--> {current.next})')
                else:
                    print(current)
                current = current.next
        else:
            print(self.head)

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def pop_begin(self):
        if self.head is not None:
            data = self.head
            self.head = self.head.next
            self.head.previous = self.tail
            self.tail.next = self.head
            self.size -= 1
            return data        
        else:
            return None
        
    def pop_end(self):
        if self.head is not None:
            data = self.tail
            self.tail = self.tail.previous
            self.tail.next = self.head
            self.head.previous = self.tail
            self.size -= 1
            return data
        else:
            return None

    def extract(self):
        if self.head is not None:
            current = self.head
            for i in range(self.size):
                yield current.data
                current = current.next
        else:
            return None

    def search(self, data):
        current = self.head
        for i in range(self.size):
            if current.data == data:
                return True
            current = current.next
        return False
