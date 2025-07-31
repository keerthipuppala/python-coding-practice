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

    '''
    def delete_by_value(self, key):
        temp = self.head
        if not temp:
            print("Empty Linked List")
            return

        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            print(f"{key} deleted from the list")
            return

        while temp and temp.data != key:
            temp = temp.next

        if not temp:
            print(f"{key} not found in the Linked List")
            return

        if temp.prev:
            temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev

        print(f"{key} deleted from the linked list")'''
    def delete_by_value(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                print(f"Deleted:{temp.data}")
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return 
            temp = temp.next
        print(f"{value} not found in the linked list")
    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")

dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_beginning(val)

dll.display()

d = int(input("Enter how many delete-by-value operations you want to perform: "))
for _ in range(d):
    val = int(input("Enter the value to delete: "))
    dll.delete_by_value(val)
    dll.display()

