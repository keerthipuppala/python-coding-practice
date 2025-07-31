class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        
        if pos <= 0:
            print("Position must be >= 1")
            return
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            print(f"{data} inserted at position 1")
            return

        current = self.head


        for _ in range(pos-2):
            if current is None:
                print("Position out of range")
                return
            current = current.next
            
        if current is None:
            print("No elements....")
            return

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node

        current.next = new_node
        print(f"{data} inserted at position {pos}")

    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")
dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    pos = int(input(f"Enter position to insert {val}: "))
    dll.insert_at_position(val, pos)

dll.display()
