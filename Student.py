# File: Student.py
# Student: Akwawo Ekpu 
# UT EID: ace2453
# Course Name: CS303E
# 
# Date: 03/01/2023
# Description of Program: This is a program used to imput grades for exam 1 and exam2 and calculate the average for individual students students.

class Student:
    def __init__(self, name, exam1=None, exam2= None):
        self.__name = name
        self.__exam1 = exam1
        self.__exam2 = exam2
        
    def getName(self):
        return self.__name

    def getExam1Grade(self):
        return self.__exam1

    def getExam2Grade(self):
        return self.__exam2

    def setExam1Grade(self, grade):
        self.__exam1 = grade
    
    def setExam2Grade(self, grade):
        self.__exam2 = grade

    def getAverage(self):
        if self.__exam1 == None or self.__exam2 == None:
            return "Some exam grades not available."
        else:
            return (self.__exam1 + self.__exam2) / 2
        
    def __str__(self):
        return "Student: " +str(self.__name) + "\n  Exam1: "+ str(self.__exam1)  +  "\n  Exam2: " + str(self.__exam2)
