from os import system

UNSET_OPTION = -1
EXIT_OPTION = 6

def display_get_choice():
    print("============Select an Option============")
    print("1. Cowsay (Guessing Game) - Causon")
    print("2. ")
    print("3. ")
    print("4. ")
    print("5. ")
    print("6. Exit")
    print("========================================")
    
    try:
        choice = int(input("Enter your choice: "))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input! Please enter a number.")
        return UNSET_OPTION


def main():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()

main()