import random

count = 0

num_rolls = int(input("How many rolls? "))
roll_list = [0] * 12

while count < num_rolls:
    if num_rolls > 0:
        roll_total = random.randint(2,12)
        roll_list[roll_total] += 1
        count += 1
        print(roll_total)

print(roll_list)

def asterick_count(roll_list):
    for item in roll_list:
        print('*' * roll_list[item])
    return

print(f'Sum of 2:{roll_list[0] * "*"}')
print(f'Sum of 3:{roll_list[1] * "*"}')
print(f'Sum of 4:{roll_list[2] * "*"}')
print(f'Sum of 5:{roll_list[3]}')
print(f'Sum of 6:{roll_list[4]}')
print(f'Sum of 7:{roll_list[5]}')
print(f'Sum of 8:{roll_list[6]}')
print(f'Sum of 9:{roll_list[7]}')
print(f'Sum of 10:{roll_list[8]}')
print(f'Sum of 11:{roll_list[9]}')
print(f'Sum of 12:{roll_list[10]}')