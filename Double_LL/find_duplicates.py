class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def display(self):
        temp = self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")

    def duplicate_count(self):
        temp = self.head
        freq = {}

        while temp:
            if temp.data in freq:
                freq[temp.data] += 1
            else:
                freq[temp.data] = 1
            temp = temp.next

        print("Duplicate values in DLL:")
        found = False
        for key in freq:
            if freq[key] > 1:
                print(f"{key} appears {freq[key]} times")
                found = True

        if not found:
            print("No duplicates found.")


dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_end(val)

dll.display()
dll.duplicate_count()
