# File: Handicap.py
# Student: Akwawo Ekpu 
# UT EID: ace2453
# Course Name: CS303E
# Date: 01/23/2023
# Description of Program: This program was made to calculate and generate the handicap and average of a given bowler.

def main():


    name = input ("\nEnter Bowler's name: ")
    game1 = int(input("Enter Game 1: "))
    game2 = int(input("Enter Game 2: "))
    game3 = int(input("Enter Game 3: "))

    average  = (game1 + game2 + game3)// 3
    if average >= 200 :
        handicap = 0
    else:
        handicap = (200 - average) * 0.8
    
    
    print("\n \nHandicap report for "+ name +":")
    print("\t" + name + "'s average is:", average)
    print("\t"+ name + "'s handicap is:", int(handicap), "\n")
    print("It's time to Bowl!")



main()

    
