#!/usr/bin/python3
""" This module defines a Node and SinglyLinkedList classes.
"""


class Node:
    """Class Node that defines a node.
    """
    def __init__(self, data, next_node=None):
        """Initialize method that stores value for private attributes.
        Args:
            data (int): data of the node.
            next_node (Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve private instance attribute data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Set private instance attribute data
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrieve private instance attribute next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set private instance attribute next_node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList defines a singly linked list .
    """
    def __init__(self):
        """Initialize method that stores value for private attributes.
        """
        self.__head = None

    def __str__(self):
        """print the entire list in stdout one node number by line.
        """
        list_str = ""
        tmp = self.__head
        while tmp is not None:
            list_str += str(tmp.data)
            if tmp.next_node is not None:
                list_str += "\n"
            tmp = tmp.next_node
        return list_str

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position
            in the list (increasing order)
        """
        node_ptr = self.__head
        while node_ptr is not None:
            if node_ptr.data > value:
                break
            prev_node_ptr = node_ptr
            node_ptr = node_ptr.next_node

        new_node = Node(value, node_ptr)
        if node_ptr == self.__head:
            self.__head = new_node
        else:
            prev_node_ptr.next_node = new_node
