###Program: Interactive ATM simulation


class User:
    def __init__(self, name, user_id, pin, checking_balance, savings_balance):
        self.name = name
        self.user_id = user_id
        self.pin = pin
        self.checking_balance = float(checking_balance)
        self.savings_balance = float(savings_balance)

    def check_balance(self):
        return f"Checking: ${self.checking_balance}\nSavings: ${self.savings_balance}"

    def withdraw(self, account, amount):
        if account == "checking" and amount <= self.checking_balance:
            self.checking_balance -= amount
            return f"Withdrawn ${amount} from Checking. Remaining: ${self.checking_balance}"
        elif account == "savings" and amount <= self.savings_balance:
            self.savings_balance -= amount
            return f"Withdrawn ${amount} from Savings. Remaining: ${self.savings_balance}"
        else:
            return "Insufficient balance!"

    def transfer(self, amount):
        if amount <= self.checking_balance:
            self.checking_balance -= amount
            self.savings_balance += amount
            return f"Transferred ${amount} to Savings.\nChecking: ${self.checking_balance}\nSavings: ${self.savings_balance}"
        else:
            return "Insufficient balance in Checking!"

    def to_string(self):
        return f"{self.name},{self.user_id},{self.pin},{self.checking_balance},{self.savings_balance}"  


def load_users(filename="atm_users.txt"):
    users = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, user_id, pin, checking, savings = line.strip().split(",")
                users[user_id] = User(name, user_id, pin, checking, savings)
    except FileNotFoundError:
        pass
    return users


def save_users(users, filename="atm_users.txt"):
    with open(filename, "w") as file:
        for user in users.values():
            file.write(user.to_string() + "\n")


def authenticate(users):
    user_id = input("Enter User ID: ")
    pin = input("Enter PIN: ")
    if user_id in users and users[user_id].pin == pin:
        print(f"Welcome {users[user_id].name}!")
        return users[user_id]
    else:
        print("Invalid User ID or PIN!")
        return None


def atm_menu(user):
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Transfer to Savings")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            print(user.check_balance())
        elif choice == "2":
            account = input("From which account? (checking/savings): ").lower()
            amount = float(input("Enter amount: "))
            print(user.withdraw(account, amount))
        elif choice == "3":
            amount = float(input("Enter amount to transfer from Checking to Savings: "))
            print(user.transfer(amount))
        elif choice == "4":
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid option! Try again.")


def main():
    users = load_users()
    user = authenticate(users)
    if user:
        atm_menu(user)
        save_users(users)  # Save updates before exiting


if __name__ == "__main__":
    main()