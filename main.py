from os import system
import causon
import franco
import efondo

UNSET_OPTION = -1
EXIT_OPTION = 6

def display_get_choice():
    print("============Select an Option============")
    print("1. Cowsay (Guessing Game) - Causon")
    print("2. Emoji (Emotion Identifier) - Franco")
    print("3. PyJokes (Chatbot) - Efondo")
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

def process_choice(choice):
    match choice:
        case 1:
            causon.start()
        case 2:
            franco.emotion_identifier()
        case 3:
            efondo.chat_bot()
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case _:
            pass

def main():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)

main()