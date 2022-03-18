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
        self.head = None
        self.tail = None
        self.size = 0
        
    def display(self, debug=False):
        if self.head is not None:
            current = self.head
            while current is not None:
                if debug:
                    print(f'{current} (--> {current.next})')
                else:
                    print(current)
                current = current.next
        else:
            print(self.tail)
            
    def push_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.size += 1
        
    def push_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        
    def search(self, data):
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def pop_begin(self):
        if self.head is not None:
            data = self.head
            self.head = self.head.next
            self.size -= 1
            return data
        else:
            return None

    def pop_end(self):
        if self.head is not None:
            data = self.tail.data
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.tail = current.next
            self.size -= 1
            return data
        else:
            return None
         
    def reverse(self):
        current = self.head
        self.tail = current
        previous_node = None
        next_node = None
        while current is not None:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
        self.head = previous_node

    def extract(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                yield current.data
                current = current.next
        else:
            return None

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
