'''
search operation where element in the node is present or not
'''

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
            return
        current = self.head
        
        while current.next:
            current = current.next
        current.next = new_node
    def search(self,key):
        pos = 1
        current = self.head
        while current:
            if current.data == key:
                print(f"{key} found in the Lind List")
                return True
            current = current.next
            pos += 1
        print(f"{key} not found in the Linked List")
        return False
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
    print("3. searching")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter the data to insert: "))
        #pos = int(input("Enter position to insert: "))
        linked_list.insert_at_end(data)
    elif choice == '2':
        linked_list.display()
    elif choice == '3':
        val = int(input("Enter the value to search: "))
        linked_list.search(val)
    elif choice == '4':
        print("Exit the operation....")
        break
    else:
        print("Invalid choice. Please try again.")
