#!/usr/bin/env python
# CSCI3202 Assignment1
# Written by Soo Park 2016


class Stack: 
    def __init__(self):
        self.list = []

    def push(self, integer):
        self.list.append(integer)
        return self.list

    def pop(self):
        size = self.checkSize()
        del self.list[size - 1]
        return self.list

    def checkSize(self):
        return len(self.list)

# final list should be [1, 2]
s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print s.list

class Node:
    def __init__(self, key, leftChild, rightChild, parent):
        self.key = key
        self.left = leftChild
        self.right = rightChild
        self.parent = parent

    def getChildren(self):
        return [self.left, self.right]

# tree looks like: [-1][0][1]
n = Node(1, 2, 3, 0)
print n.getChildren()
print n.parent

