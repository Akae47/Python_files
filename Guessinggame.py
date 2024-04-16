# File: GuessingGame.py
# Student: Akwawo Ekpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date: 02/11/2023
# Description of Program: 

import random

def main(initialnumber = None):
    print("\nWelcome to the guessing game! Good luck!")

    count = 0 
    val = None 

    while count >= 0:
        Q = input("\nAre you ready to play (Y/N): ")
        if Q == "N":
            count -= 1
            print("\nWell, come again later. Goodbye!\n")
            break

        elif Q != "N" and Q != "Y":
            print("\nSorry, I didn't recognize your answer. Try again!")
            

        elif Q == "Y":
            
            num = 10
            numm = 11
            initialnumber = random.randint(1,999)
            print("\nSee if you can guess the 'secret number'! ")
            while num > 0:
                count += 1
                number = int(input("\nEnter an integer from 1 to 999: "))
                if number < 1 or number > 1000:
                    print ("That's an illegal guess. Try again! You have" ,num, "guesses left.")


                elif number == initialnumber:
                    print("Congratulations, you got it! You took" , count , "guesses!")
                    count = 0
                    break
                    
                else:
                    num -= 1
                    numm -= 1
                    if number > initialnumber:
                        print("Your guess is too high. Try again! You have" , num , "guesses left.")
                            
                    else:
                        print("Your guess is too low. Try again! You have" , num , "guesses left.")

                    
            print("Sorry! You took too many guesses. The answer was" , initialnumber, ". Better luck next time!\n")
                    
                        
                            
        


main()
