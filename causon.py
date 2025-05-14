import random
import cowsay
from os import system

UNSET_OPTION = -1
EXIT_OPTION = 4
EASY_ENEMY_COUNT = 5
AVERAGE_ENEMY_COUNT = 10
HARD_ENEMY_COUNT = 15
MAX_HEALTH = 3

def display_get_choice():
    print("=====Cowsay Guessing Game=====")
    print("=====Select a Difficulty======")
    print("1. Easy")
    print("2. Average")
    print("3. Hard")
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
            play(EASY_ENEMY_COUNT)
        case 2:
            play(AVERAGE_ENEMY_COUNT)
        case 3:
            play(HARD_ENEMY_COUNT)
        case 4:
            system("cls")
            
def play(number_of_enemies):
    enemies_list = random.sample(cowsay.char_names, number_of_enemies)
    lives = MAX_HEALTH
    while lives > 0:
        # TODO (Miko): add guessing functionality
        pass

def start():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)