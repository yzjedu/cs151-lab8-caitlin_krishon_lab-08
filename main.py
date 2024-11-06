# Programmers: Krishon and Caitlin
# Course: CS151, Professor Zee
# Due Date: November 5, 2024
# Lab Assignment: Lab 08
# Problem Statement: We needed to create a program that counted the result of rolls of dice
# Data In: Number of rolls
# Data Out: List of sums, total of rolls, and tally of sums
# Credits: None other than class notes

# Import random function into program
import random

# Purpose: Run the main program and invokes the functions, roll_counter and sum_tally
# Parameters: [None]
# Return: Number of rolls and roll list

def main():
    roll_list = [0] * 11
    num_rolls = int(input("How many rolls? "))
# Purpose: Finds the total of the pair of dice being rolled and adds the total to the list of rolls
# Parameters: [None]
# Return: List of rolls

    def roll_counter():
        count = 0
        while count < num_rolls:
            if num_rolls > 0:
                roll_total = random.randint(2,12)
                roll_list[roll_total - 2] += 1
                count += 1
        return roll_list

# Purpose: Outputs distribution of rolls, outputs list of rolls, and tallies occurrences of dice sums
# Parameters: [None]
# Return: [None]

    def sum_tally():
        print(f'Rolling {num_rolls} pairs of dice')
        print(roll_list)
        print(f'Sum of 2:{roll_list[0] * "*"}')
        print(f'Sum of 3:{roll_list[1] * "*"}')
        print(f'Sum of 4:{roll_list[2] * "*"}')
        print(f'Sum of 5:{roll_list[3] * "*"} ')
        print(f'Sum of 6:{roll_list[4] * "*"}')
        print(f'Sum of 7:{roll_list[5] * "*"}')
        print(f'Sum of 8:{roll_list[6] * "*"}')
        print(f'Sum of 9:{roll_list[7] * "*"}')
        print(f'Sum of 10:{roll_list[8] * "*"}')
        print(f'Sum of 11:{roll_list[9] * "*"}')
        print(f'Sum of 12:{roll_list[10] * "*"}')
        return

    roll_counter()
    sum_tally()
    return num_rolls, roll_list

# Invokes the main function
main()