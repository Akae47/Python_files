# File: FindPrimeFactors.py
# Student: Akwawo EKpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date:21/03/2023
# Description of Program: This is a program that decideds whether a number is aprime and then prints the prime numbers.



import math

def isPrime(num):
    if (num < 2) or (num % 2 == 0):
        return num == 2
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

def findprime(num):
    if num % 2 == 0:
        num -= 1
    guess = num + 2

    while (not isPrime(guess)):
        guess += 1
    return guess if guess != num else num

def primeFactorization(num):
    primes = []
    if isPrime(num):
        return [num]
    else:
        d = 2
        while num > 1:
            if num % d == 0:
                primes.append(d)
                num = num/ d
            else:
                d = findprime(d)
        return primes

def main():
    print("Find Prime Factors:")
    while True:
        num = int(input("Enter a positive integer (or 0 to stop): "))
        if num == 0:
            print("Goodbye!\n")
            break
        elif num == 1:
            print("  1 has no prime factorization.\n")
        elif num < 0:
            print("  Negative integer entered. Try again.\n")
        else:
            primes = primeFactorization(num)
            print("The prime factorization of", num, "is:", primes, "\n")

main()

