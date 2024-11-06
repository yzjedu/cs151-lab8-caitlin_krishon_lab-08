import random
# Programmers:  Caitlin Burns and Krishon Pinkins
# Course:  CS151, Professor Zee
# Due Date: 11/6/2024
# Lab Assignment: 8
# Problem Statement: This code allows a user to enter a number of rolls and the program will output the total
# Data In: number of rolls
# Data Out: total tally of rolls
# Credits: this code is based on the guidelines from the read me file

roll_list = [0] * 13

# Purpose:  sets number of rolls
# Parameters: none
# Return: number of rolls
def number_rolls():
    number =input('how many rolls do you want?: ')
    number = int(number)
    while number < 1:
        print('Invalid number. Try again')
        number = input('how many rolls do you want?: ')
        number = int(number)
    return number

# Purpose:  sets roll total and the list
# Parameters: count
# Return: the roll total
def roll_total(count):
    roll = random.randint(1, 6) + random.randint(1, 6)
    roll_list[roll] += 1
    count +=1
    return roll

# Purpose:  prints the asterisks for the score
# Parameters: roll list
# Return: none
def asterisk_count(roll_list):
    print(f'Sum of 2:{roll_list[0] * "*"}')
    print(f'Sum of 3:{roll_list[1] * "*"}')
    print(f'Sum of 4:{roll_list[2] * "*"}')
    print(f'Sum of 5:{roll_list[3] * "*"}')
    print(f'Sum of 6:{roll_list[4] * "*"}')
    print(f'Sum of 7:{roll_list[5] * "*"}')
    print(f'Sum of 8:{roll_list[6] * "*"}')
    print(f'Sum of 9:{roll_list[7] * "*"}')
    print(f'Sum of 10:{roll_list[8] * "*"}')
    print(f'Sum of 11:{roll_list[9] * "*"}')
    print(f'Sum of 12:{roll_list[10] * "*"}')

# Purpose: allows user to roll again
# Parameters: none
# Return: choice
def roll_again():
    choice = input('Would you like to roll again? (y/n): ')
    choice = choice.lower()
    return choice

# Purpose: runs game
# Parameters: none
# Return: none
def game():
    print('This program allows you to roll two die and outputs your running total')
    count = 0
    number = number_rolls()
    while count < number:
        roll = roll_total(count)
        count += 1
    print(roll_list)
    asterisk_count(roll_list)

# Purpose: runs main function
# Parameters: none
# Return: none
def main():
    game()
    choice = roll_again()
    while choice == 'y':
        game()
        choice = roll_again()
    print('Thank you for playing!')




main()