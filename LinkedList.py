# Python program to create Linked List and perform various operations on it

# Creating a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def traverse_to_index(self, index):
        current_node = self.head
        for i in range(index):
            current_node = current_node.next
        return current_node
    
    def insert(self, index, data):
        if index >= self.length:
            self.append(data)
        elif index == 0:
            self.prepend(data)
        else:
            new_node = Node(data)
            leader = self.traverse_to_index(index-1)
            new_node.next = leader.next
            leader.next = new_node
            self.length += 1

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=' ')
            current_node = current_node.next
    
    def pop(self):
        leader = self.traverse_to_index(self.length-2)
        leader.next = None
        self.tail = leader
        self.length -= 1
    
    def remove_first(self):
        self.head = self.head.next
        self.length -= 1
    
    def remove(self, index):
        leader = self.traverse_to_index(index-1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1