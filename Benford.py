# File: Benford.py
# Student: Akwawo Ekpu
# UT EID: ace2453
# Course Name: CS303E
# 
# Date: 03/31/2023
# Description of Program: This is a program that uses data from the census data file to prove bENFORDS LA.


import os.path
def main():
    filename = input("Enter the name of a file of census data: ")

    if not os.path.exists(filename):
        print("File does not exist")
    else:
        digits = [0] * 10
        total_count = 0
        unique_counts = set()
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split()
                population = parts[-1]
                if population.isdigit():
                    total_count += 1
                    unique_counts.add(int(population))
                    first_digit = int(str(population)[0])
                    digits[first_digit] += 1

        with open("benford.txt", 'w') as f:
            f.write("Total number of cities: {}\n".format(total_count))
            f.write("Unique population counts: {}\n".format(len(unique_counts)))
            f.write("First digit frequency distributions:\n")
            f.write("Digit\tCount\tPercentage\n")
            for i in range(1, 10):
                count = digits[i]
                percentage = count / total_count * 100
                f.write("{}\t{}\t{:.1f}\n".format(i, count, percentage))

        print("Output written to benford.txt")

main()
