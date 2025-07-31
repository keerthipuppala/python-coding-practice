# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List class
class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node

        new_node.next = self.head  # Point to current head
        if self.head:
            self.head.prev = new_node  # Update previous link of old head
        self.head = new_node  # Move head to new node

    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")

# Main
dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_beginning(val)

dll.display()
