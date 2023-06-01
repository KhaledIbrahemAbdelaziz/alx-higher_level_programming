#!/usr/bin/python3
"""representing a node"""


class Node:
    """define singly linked list node"""

    def __init__(self, data, next_node=None):
        """Initialize the data and the pointer next of the node
        args:
        data (int): the value in the node.
        next_node (pointer): a pointer to the next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve it: (the data)"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """set it: the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve it: (the next node pointer)"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """set it: the next node pointer"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """representing the list"""

    def __init__(self):
        """initialize the head of the list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
        in the list (increasing order)"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and 
                    temp.next_node.data < value):
                temp = temp.next_node
                new.next_node = temp.next_node
                temp.next_node = new

    def __str__(self):
        """initialize the print values"""
        value = []
        temp = self.__head
        while temp is not None:
            value.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(value))
