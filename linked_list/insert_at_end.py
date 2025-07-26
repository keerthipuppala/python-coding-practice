class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"{data} inserted at end / will be first node")
            return
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node
        print(f"{data} inserted at end")
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
    print("\nLinkedList - Insert at Beginning Menu")
    print("1. Insert at Beginning")
    print("2. Display")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter the data: "))
        linked_list.insert_at_end(data)
    elif choice == '2':
        linked_list.display()
    elif choice == '3':
        print("Exiting the operation...")
        break
    else:
        print("Invalid choice. Please try again.")
