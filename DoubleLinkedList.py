# -*- coding: utf-8 -*-
with open (r'H:\04_Python\EUCountries.txt') as file:
    countries = file.read()
countries = countries.split('\n')

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
    
    def display(self, debug=False):
        if self.header is not None:
            current = self.header
            while current is not None:
                if debug:
                    print(f'({current.previous} <--) {current} (--> {current.next})')
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
            current.next.previous = current
        self.size += 1

    def push_begin(self, data):
        node = Node(data)
        if self.header is None:
            self.header = node
        else:
            current = self.header
            while current.previous is not None:
                current = current.previous
            current.previous = node
            current.previous.next = current
            self.header = current.previous
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
            self.header.previous = None
            self.size -= 1
            return data
        else:
            return None

    def pop_end(self):
        if self.header is not None:
            current = self.header
            while current.next is not None:
                current = current.next
            data = current.data
            current.previous.next = None
            self.size -= 1
            return data
        else:
            return None

    def reverse(self):
        previous_node = None
        current = self.header
        next_node = None
        while current is not None:
            next_node = current.next
            current.next = previous_node
            current.previous = next_node
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

linkedlist = LinkedList()
for i in countries:
    linkedlist.push_begin(i)

print(linkedlist.pop_begin())
linkedlist.display(debug=True)