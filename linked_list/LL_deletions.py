class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
        else:
            print("Deleted from beginning:", self.head.data)
            self.head = self.head.next

    # Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
        elif self.head.next is None:
            print("Deleted from end:", self.head.data)
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            print("Deleted from end:", temp.next.data)
            temp.next = None

    # Delete by value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == value:
            print("Deleted node with value:", value)
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found.")
        else:
            print("Deleted node with value:", value)
            temp.next = temp.next.next

    # Delete by position (0-based index)
    def delete_by_position(self, pos):
        if self.head is None:
            print("List is empty.")
            return

        if pos == 0:
            print("Deleted node at position 0:", self.head.data)
            self.head = self.head.next
            return

        temp = self.head
        count = 0
        while temp.next and count < pos - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            print("Position out of range.")
        else:
            print(f"Deleted node at position {pos}:", temp.next.data)
            temp.next = temp.next.next

    # Display list
    def display(self):
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Main Program
ll = LinkedList()

while True:
    print("\nMenu:")
    print("1. Insert")
    print("2. Delete from beginning")
    print("3. Delete from end")
    print("4. Delete by value")
    print("5. Delete by position")
    print("6. Display")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        data = int(input("Enter data: "))
        ll.insert(data)
    elif choice == '2':
        ll.delete_from_beginning()
    elif choice == '3':
        ll.delete_from_end()
    elif choice == '4':
        val = int(input("Enter value to delete: "))
        ll.delete_by_value(val)
    elif choice == '5':
        pos = int(input("Enter position to delete: "))
        ll.delete_by_position(pos)
    elif choice == '6':
        ll.display()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Try again.")
