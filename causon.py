import random
import cowsay
from os import system

UNSET_OPTION = -1
EXIT_OPTION = 4
EASY_CHARACTER_COUNT = 5
AVERAGE_CHARACTER_COUNT = 10
HARD_CHARACTER_COUNT = 15
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
            play(EASY_CHARACTER_COUNT)
        case 2:
            play(AVERAGE_CHARACTER_COUNT)
        case 3:
            play(HARD_CHARACTER_COUNT)
        case 4:
            system("cls")
            
def play(number_of_characters):
    characters_list = random.sample(cowsay.char_names, number_of_characters)
    lives = MAX_HEALTH
    while lives > 0:
        system("cls")
        guess = display_get_guess(characters_list)
        

def display_get_guess(characters_list):
    for number, character in enumerate(characters_list, 1): 
        print(f"{number}. {character}")
        
    try:
        choice = int(input("Enter your choice: "))
        system("cls")
        return choice
    except ValueError:
        system("cls")
        print("Invalid input! Please enter a number.")
        return UNSET_OPTION
    

def start():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)