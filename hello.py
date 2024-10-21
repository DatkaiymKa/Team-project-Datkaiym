def display_menu():
    print("Please choose your option from the list below:")
    print("1. Learn Python")
    print("2. Learn Java")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")
    print("6. Read a book")
    print("7. Watch a movie")
    print("8. Exercise")
    print("9. Play video games")
    print("0. Exit")

def handle_choice(choice):
    if choice == '1':
        print("You chose to Learn Python!")
    elif choice == '2':
        print("You chose to Learn Java!")
    elif choice == '3':
        print("You chose to Go swimming!")
    elif choice == '4':
        print("You chose to Have dinner!")
    elif choice == '5':
        print("You chose to Go to bed!")
    elif choice == '6':
        print("You chose to Read a book!")
    elif choice == '7':
        print("You chose to Watch a movie!")
    elif choice == '8':
        print("You chose to Exercise!")
    elif choice == '9':
        print("You chose to Play video games!")
    elif choice == '0':
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid option, please choose a valid number.")

def main():
    choice = None
    while choice != '0':
        display_menu()
        choice = input("Enter the number of your choice: ")
        handle_choice(choice)

if __name__ == "__main__":
    main()