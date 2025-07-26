class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node    
    def deletevalue(self,key):
        current  = self.head
        if not current:
            print("Empty Linked List")
            return 
        if current.data == key:
            self.head = current.next
            print(f"{key} deleted from the list")
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            print(f"{key} not found in the Lined List")
            return
        prev.next = current.next
        print(f"{key} deleted from the linked list")
        
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
    print("1. Insert ")
    print("2. Display")
    print("3. delete by value")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter the data: "))
        linked_list.insert_at_beginning(data)
    elif choice == '2':
        linked_list.display()
    elif choice == '3':
        key  = int(input("Enter the value to delete: "))
        linked_list.deletevalue(key)
        
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
