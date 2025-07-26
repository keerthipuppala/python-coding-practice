class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos <= 0:
            print("Position must be >= 1")
            return
        if pos == 1:   #begin insert
            new_node.next = self.head
            self.head = new_node
            print(f"{data} inserted at position 1")
            return
        current = self.head
        count = 1
        while current and count < pos - 1:
            current = current.next
            count += 1
        if not current:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node
        print(f"{data} inserted at position {pos}")

    def display(self):
        current = self.head
        if not current:
            print("Linked list is empty")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()

while True:
    print("\nLinkedList - Insert at Position Menu")
    print("1. Insert at Position")
    print("2. Display")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter the data: "))
        pos = int(input("Enter position to insert: "))
        linked_list.insert_at_position(data, pos)
    elif choice == '2':
        linked_list.display()
    elif choice == '3':
        print("Exiting the operation...")
        break
    else:
        print("Invalid choice. Please try again.")
