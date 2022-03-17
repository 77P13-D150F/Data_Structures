#/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.header = None
        self.size = 0
        
    def display(self, debug=False):
        if self.header is not None:
            current = self.header
            while current is not None:
                if debug:
                    print(f'{current} (--> {current.next})')
                else:
                    print(current)
                current = current.next
        else:
            print(self.header)
            
    def push_end(self, data):
        node = Node(data)
        if self.header is None:
            self.header = node
        else:
            current = self.header
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1
        
    def push_begin(self, data):
        node = Node(data)
        if self.header is None:
            self.header = node
        else:
            node.next = self.header
            self.header = node
        self.size += 1
        
    def search(self, data):
        current = self.header
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def pop_begin(self):
        if self.header is not None:
            data = self.header
            self.header = self.header.next
            self.size -= 1
            return data
        else:
            return None

    def pop_end(self):
        if self.header is not None:
            current = self.header
            while current.next.next is not None:
                current = current.next
            data = current.next.data
            current.next = None
            self.size -= 1
            return data
        else:
            return None
         
    def reverse(self):
        current = self.header
        previous_node = None
        next_node = None
        while current.next is not None:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
        self.header = previous_node

    def extract(self):
        if self.header is not None:
            current = self.header
            while current is not None:
                yield current.data
                current = current.next
        else:
            return None

    def clear(self):
        self.header = None
        self.size = 0

        
