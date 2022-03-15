from Node import *

class LinkedList:
    def __init__(self):
        self.first = None
        self.length = 0

    def add(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
        else:
            temp = self.first + 10 #this will blow up
            while temp.next is not None:
                temp = temp.next
            temp.set_next(new_node)
        self.length += 1
        print(self.length) #made change here


    def print(self):
        temp = self.first
        while temp is not None:
            print(temp.value, end = " ")
            temp = temp.next
        print()

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0:
            raise Exception("Index out of bounds")
        elif index == 0:
            new_node.next = self.first
            self.first = new_node
        else:
            temp = self.first
            for _ in range(index - 1):
                if temp is None or temp.next is None:
                    raise Exception("Index out of bounds")
                else:
                    temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length += 1

    def delete(self, index):
        if index < 0:
            raise Exception("Index out of bounds")
        elif index == 0:
            self.first = self.first.next
        else:
            temp = self.first
            for _ in range(index -1):
                if temp is None or temp.next.next is None:
                    raise Exception("Index out of bounds")
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1

    def get(self,index):
        temp = self.first
        for i in range(index):
            if temp is None:
                raise Exception("Index out of bounds")
            temp = temp.next
        print(str(tamp.value) + " " + str(index))
        return temp.value

    def getLength(self):
        return self.length

