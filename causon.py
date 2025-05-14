import random
import cowsay
from os import system

UNSET_OPTION = -1
EXIT_OPTION = 4
EASY_CHARACTER_COUNT = 5
AVERAGE_CHARACTER_COUNT = 10
HARD_CHARACTER_COUNT = 15
MAX_HEALTH = 3
MIN_SCORE = 0

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
    score = MIN_SCORE
    while lives > 0:
        if run_round(characters_list, number_of_characters):
            score += 1
        else:
            lives -= 1

def display_get_guess(characters_list):
    for number, character in enumerate(characters_list, 1): 
        print(f"{number}. {character}")
        
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except ValueError:
        print("Invalid input! Please enter a number.")
        return UNSET_OPTION

def run_round(characters_list, number_of_characters):
    system("cls")
    print("Pick who will show up!")
    character_index = random.randrange(len(characters_list))
    character = characters_list[character_index]
    guess = display_get_guess(characters_list) - 1 # to match the index
    
    if guess > number_of_characters and guess < 1:
        print("You didn't pick a valid choice, -1 life.")
        return False
    elif guess != character_index:
        print(cowsay.get_output_string(character, f"No, I'm {character}."))
        input("Press Enter to continue.")
        return False
    else:
        print(f"guess: {guess}, charIndex: {character_index}")
        print(cowsay.get_output_string(character, "You got me!"))
        input("Press Enter to continue.")
        return True

def start():
    choice = UNSET_OPTION
    while choice != EXIT_OPTION:
        choice = display_get_choice()
        process_choice(choice)