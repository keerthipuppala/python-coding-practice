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
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_by_value(self, key):
        curr = self.head
        if not curr:
            print("List is empty.")
            return
        if curr.data == key:
            self.head = curr.next
            print(f"Deleted {key}")
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if not curr:
            print(f"{key} not found.")
            return
        prev.next = curr.next
        print(f"Deleted {key}")

    def search(self, key):
        curr = self.head
        pos = 0
        while curr:
            if curr.data == key:
                return pos
            curr = curr.next
            pos += 1
        return -1

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def display(self):
        if not self.head:
            print("List is empty.")
            return
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

# Driver menu
if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\nMenu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display")
        print("5. Find Middle")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            val = int(input("Enter value to insert: "))
            ll.insert_at_end(val)
        elif choice == "2":
            val = int(input("Enter value to delete: "))
            ll.delete_by_value(val)
        elif choice == "3":
            val = int(input("Enter value to search: "))
            pos = ll.search(val)
            if pos != -1:
                print(f"Found at position {pos}")
            else:
                print("Not found")
        elif choice == "4":
            print("Linked List:")
            ll.display()
        elif choice == "5":
            mid = ll.find_middle()
            print("Middle node is:", mid if mid is not None else "List is empty")
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")
