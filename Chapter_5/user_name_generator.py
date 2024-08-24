###Program: Username Generator

def main()->None:
    print("***** User name Generator *****\n")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    user_name = first.lower()[0] + last.lower()[:7]
    print(f"Username: {user_name}")

main()
