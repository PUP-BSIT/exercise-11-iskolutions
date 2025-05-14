import cowsay
from os import system

UNSET_OPTION = -1
EXIT_OPTION = 4

def display_get_choice():
    print("=====Cowsay Guessing Game=====")
    print("=====Select a Difficulty======")
    print("1. Easy")
    print("2. Average")
    print("3. Difficult")
    print("4. Exit")
    print("==============================")
    
    try:
        choice = int(input("Enter your choice: "))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input! Please enter a number.")
        return UNSET_OPTION
    
def process_choice(choice):
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            system("cls")

def start():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)