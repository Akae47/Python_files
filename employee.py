#  File: Employee.py
#  Student Name: Akwawo Ekpu
#  Student UT EID: ace2453

# Decorator to round values to one decimal place


#This is the base class representing an Employee.
class Employee:
    def __init__(self, **kwargs):\
        #Employee initializer with name, ID, and salary attributes
        self._name = kwargs.get('name')
        self._id = kwargs.get('id')
        self._salary = kwargs.get('salary')


    @property
    def salary(self):
        #Getter for salary
        return self._salary
        

    @salary.setter
    def salary(self, salary):
        #Setter for salary
        self._salary = salary

    @property
    def name(self):
        # Getter for name
        return self._name

    @property
    def id(self):
        # Getter method for ID
        return self._id

    def __str__(self):
        # String method
        return f"Employee Name: {self._name}, ID: {self._id}, Salary: {self._salary}"


class Permanent_Employee(Employee):
    #this is a derived class for Employee

    def __init__(self, **kwargs):
        #Permenant Employee initializer with self benefits and Employee attributes
        super().__init__(**kwargs)
        self._benefits = kwargs.get('benefits', [])

    def cal_salary(self):
        # Calculator of the salary and benefits
        base_salary = self._salary
        if "health_insurance" in self._benefits:
            return base_salary * 0.9
        elif "retirement" in self._benefits:
            return base_salary * 0.8
        elif ("health_insurance" in self._benefits) and ("retirement" in self._benefits):
            return base_salary * 0.7
        else:
            return base_salary

    @property
    def benefits(self):
        #Getter for benefits
        return self._benefits

    @benefits.setter
    def benefits(self, benefits):
        #Setter for benefits
        self._benefits = benefits

    def __str__(self):
        #string returner
        return f"Permanent Employee Name: {self._name}, ID: {self._id}, Salary: {self._salary}"


class Manager(Employee):
    #This is the derived class of Employe that represents the manager
    def __init__(self, **kwargs):
        #Manager initializer with bonus attributes
        super().__init__(**kwargs)
        self._bonus = kwargs.get('bonus', 0)

    def cal_salary(self):
        #Calculate the salary and the bonus
        return self._salary + self._bonus

    @property
    def bonus(self):
        #getter for bonus
        return self._bonus

    def __str__(self):
        #string returner
        return f"Manager Name: {self._name}, ID: {self._id}, Salary: {self._salary}"


\
class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        #Temporary employee initializer with Employee attribute and hours
        super().__init__(**kwargs)
        self._hours = kwargs.get('hours', 0)

    def cal_salary(self):
        # Calculate the salary using hours worked
        return self._salary * self._hours

    def __str__(self):
        # String  for the temporary employee object
        return f"Temporary Employee Name: {self._name}, ID: {self._id}, Salary: {self._salary}"


class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        #Consultant initializer with trips and temporary employee attribute
        super().__init__(**kwargs)
        self._trips = kwargs.get('trips', 0)

    def cal_salary(self):
        # Calculate the salary using  hours worked and trips made
        return (self._salary * self._hours) + (self._trips * 1000)

    def __str__(self):
        # String for the Consultant 
        return f"Consultant Name: {self._name}, ID: {self._id}, Salary: {self._salary}"


class Consultant_Manager(Consultant, Manager):
    #consulatant manager initializer with consulatant and manager  atributes
    def __init__(self,  **kwargs):
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)

    def cal_salary(self):
        #Calculate the salary using hours worked, trips made, and bonus
        return (self._salary * self._hours) + (self._trips * 1000) + self._bonus

    def __str__(self):
        # String for sonsutant manager
        return f"Consultant Manager Name: {self._name}, ID: {self._id}"

''' ##### DRIVER CODE #####
    ##### Do not change. '''


def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:",  matt.cal_salary())


if __name__ == "__main__":
    main()
