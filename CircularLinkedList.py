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
        self.header = None
        self.size = 0
        
    def push_end(self, data):
        node = Node(data)
        if self.header is None:
            self.header = node
            self.header.next = node
            self.header.previous= node
        else:
            current = self.header
            while current.next is not self.header:
                current = current.next
            current.next = node
            current.next.previous = current
            current.next.next = self.header
            self.header.previous = current.next
        self.size += 1

    def push_begin(self, data):
        node = Node(data)
        if self.header is None:
            self.header = node
            self.header.next = node
            self.header.previous = node
        else:
            current = self.header
            while current.previous is not self.header:
                current = current.previous
            current.previous = node
            current.previous.next = current
            current.previous.previous = self.header
            self.header.next = current.previous
        self.size += 1
    
    def rotate(self, n=0):
        current = self.header
        if n > 0:
            for i in range(n):
                current = current.next
        elif n < 0:
            for i in range(-1 * n):
                current = current.previous
        else:
            pass
        self.header = current
   
    def reverse(self):
        previous_node = self.header.previous
        current = self.header
        next_node = self.header.next
        for i in range(self.size):
            next_node = current.next
            current.next = previous_node
            current.previous = next_node
            previous_node = current
            current = next_node
        self.header = previous_node
        
    def display(self, debug=False):
        if self.header is not None:
            current = self.header
            for i in range(self.size):
                if debug:
                    print(f'({current.previous} <--) {current} (--> {current.next})')
                else:
                    print(current)
                current = current.next
        else:
            print(self.header)

    def clear(self):
        self.header = None
        self.size = 0
    
    def pop_begin(self):
        if self.header is not None:
            current = self.header
            while current.next is not self.header:
                current = current.next
            current.next = self.header.next
            data = self.header.data
            self.header = self.header.next
            self.header.previous = self.header.previous.previous
            self.size -= 1
            return data        
        else:
            return None
        
    def pop_end(self):
        if self.header is not None:
            current = self.header
            while current.next.next is not self.header:
                current = current.next
            data = current.next.data
            current.next = self.header
            self.header.previous = current
            self.size -= 1
            return data
        else:
            return None

    def extract(self):
        if self.header is not None:
            current = self.header
            for i in range(self.size):
                yield current.data
                current = current.next
        else:
            return None

    def search(self, data):
        current = self.header
        for i in range(self.size):
            if current.data == data:
                return True
            current = current.next
        return False

