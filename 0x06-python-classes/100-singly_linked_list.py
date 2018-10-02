#!/usr/bin/python3
""" define singly linked list components """


class Node:
    """ a node in a singly-linked list """

    def __init__(self, data, next_node=None):
        """ init node instance """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ data getter """
        return self.__data

    @data.setter
    def data(self, value):
        """ data setter """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """ next_node getter """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ next_node setter """
        if (not isinstance(value, Node) and value is not None):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """ singly linked list """

    def __init__(self):
        """ init linked list """
        self.__head = None

    def sorted_insert(self, value):
        """ sorted insert, ascending order """
        new_node = Node(value, self.__head)
        if self.__head is None or new_node.data < self.__head.data:
            self.__head = new_node
        else:
            p = self.__head
            new_node.next_node = p.next_node
            while (new_node.next_node is not None):
                if new_node.data > new_node.next_node.data:
                    p = new_node.next_node
                    new_node.next_node = p.next_node
                else:
                    break
            p.next_node = new_node

    def __str__(self):
        """ printable """
        p = self.__head
        str = ""
        while (p is not None):
            str += "{}".format(p.data)
            p = p.next_node
            if p is not None:
                str += "\n"
        return str
