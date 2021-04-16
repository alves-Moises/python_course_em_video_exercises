#tem mto #q1 week 8
import random

def main():
    roll_count = count_input()
    roll_result = roll(roll_count)
    print("roll result")
    print(roll_result)

def count_input():
    valid = False
    while not valid:
        try:
            count = int(input("how many times dice rolled:"))
        except ValueError:
            print(" non numeric data")
        else:
            valid = True
    return count

def roll(number_of_rolls):
    roll_result = []
    for i in range(number_of_rolls):
        dice_roll = int(random.randint(1, 6))
        roll_result.append(dice_roll)
    return roll_result
main()