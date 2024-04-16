# File: Zeller.py
# Student: Ekpu, Akwawo
# UT EID: ace2453
# Course Name: CS303E
# 
# Date: 02/03/2023
# Description of Program: This is a program made to generate the day of the week of a given date using the Zellers Congruence.

def Zeller():
    K = 0
    J = 0
    y = int(input("\nEnter year(e.g., 2008): "))
    if y <= 1752:
        print("Year must be > 1752.  Illegal year entered:",y,"\n")
        
    else:
        m = int(input(("Enter month(1-12): ")))
        if m < 1 or m > 12:
            print("Month must be in [1..12]. Illegal month entered:",m,"\n")
    
            
        else:
            if m < 3:
                m += 12
                y -=  1
            d = int(input(("Enter day of the month(1-31): ")))
            if d < 1 or d >31:
                print("Day must be in [1..31]. Illegal day entered:",d,"\n")
            else:
                K = (y % 100)
                J = y // 100
                h = ( d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5*J ) % 7
                if  h == 0:
                    print("Day of the week is Saturday\n")
                elif h == 1:
                    print("Day of the week is Sunday\n")
                elif h == 2:
                    print("Day of the week is Monday\n")
                elif h == 3:
                    print("Day of the week is Tuesday\n")
                elif h == 4:
                    print("Day of the week is Wednesday\n")
                elif h == 5:
                    print("Day of the week is Thursday\n")
                elif h == 6:
                    print("Day of the week is Friday\n")
              
        
                



    


Zeller()
                
            

