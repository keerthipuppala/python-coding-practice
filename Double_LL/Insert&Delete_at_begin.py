#Insertion begining & delete at begin
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)  
        new_node.next = self.head  
        if self.head:
            self.head.prev = new_node  
        self.head = new_node
    
    def BackTraverse(self):
        print("Values for traversing backward....")
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end="<-->")
            temp = temp.prev
        print("None")
    def Delete_at_Begining(self):
        if not self.head:
            print("Cant perform delete in an empty list....")
        print(f"Deleted:{self.head.data}")
        self.head = self.head.next
        if self.head:
            self.head.prev = None
            
    
    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_beginning(val)
dll.display()
d = int(input("Enter how many times you want to perform delete operation:"))
for _ in range(d):
    dll.Delete_at_Begining()
    dll.display()
dll.BackTraverse()
