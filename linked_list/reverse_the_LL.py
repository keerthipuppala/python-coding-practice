class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next   
            current.next = prev        
            prev = current             
            current = next_node        
        self.head = prev
        print("Linked list has been reversed.")
    def display(self):
        if not self.head:
            print("Linked list is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()

n = int(input("How many elements to insert? "))
for i in range(n):
    data = int(input(f"Enter element {i+1}: "))
    ll.insert_at_end(data)

print("\nOriginal Linked List:")
ll.display()

ll.reverse()

print("\nReversed Linked List:")
ll.display()
