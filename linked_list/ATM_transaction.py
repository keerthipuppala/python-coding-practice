class Transaction:
    def __init__(self, transaction_type, amount):
        self.type = transaction_type
        self.amount = amount
        self.next = None

class TransactionHistory:
    def __init__(self):
        self.head = None

    def add_transaction(self, transaction_type, amount):
        nn = Transaction(transaction_type, amount)
        if not self.head:
            self.head = nn
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nn
        print(f"{transaction_type} of Rs. {amount} recorded...")

    def show_history(self):
        if not self.head:
            print("No transactions found...")
            return
        print("\n--- Transaction History ---")
        current = self.head
        count = 1
        while current:
            print(f"{count}. {current.type} of Rs. {current.amount}")
            current = current.next
            count += 1

    def get_balance(self):
        balance = 0
        current = self.head
        while current:
            if current.type.lower() == "deposit":
                balance += current.amount
            elif current.type.lower() == "withdraw":
                balance -= current.amount
            current = current.next
        return balance

history = TransactionHistory()
while True:
    print("\n----- ATM Transaction Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Show Transaction History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        history.add_transaction("Deposit", amount)
        print("Deposit successful.")
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        balance = history.get_balance()
        if amount > balance:
            print("Insufficient balance!")
        else:
            history.add_transaction("Withdraw", amount)
            print("Withdrawal successful.")
    elif choice == "3":
        balance = history.get_balance()
        print(f"Your current balance is: Rs. {balance}")
    elif choice == "4":
        history.show_history()
    elif choice == "5":
        print("End of the transaction --- Exit")
        break
    else:
        print("Invalid choice. Please choose only (1-5).")
