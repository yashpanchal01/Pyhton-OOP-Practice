# class Variables can be accessed Through Name of any object in the of the class or Name of Class(Which is recommended)
# Instances = Objects of Class     Therefore Instance variables are Variables defined inside the constructors
# Constructor is a special type of Method similar to a function initialized by '__init__'    
# 
# asume 'self' Argrument is NAME OF THE CLASS
# 
# EX:

# SPECIAL TYPE OF METHOD(CONSTRUCTOR) --->    def __init__(self, Argument1, Argument2)
#                                                 self.Argument1 = Argument1 
#                                                 self.Argument2 = Argument2 
#
#           METHOD(NOT A CONSTRUCTOR) --->    def Drive_car():
#                                                 self.argument1 = argument1

# 
# self reference to object we are currently working with. 

# to access any Class variable in side Methods, Use this syntaxt ---> calss_name.Variable_name
# Constructors AND Arguments AND Methods DIFFERENCE ? ---> cleared 

class student:

    Graduation_Year = 2027
    Number_of_Students = 0

    def __init__(self, NAME, AGE):
        self.NAME = NAME 
        self.AGE = AGE
        student.Number_of_Students += 1 


student1 = student("YASH", 20)
student2 = student("sam", 24)
student3 = student("matthew", 19)
student4 = student("yola",21)

# print("Name of the student1 is " + student1.NAME + " Will Graduate in year " + str(student1.Graduation_Year)) # ---> This works 

# print("Name of the student1 is " + student1.NAME + "Will Graduate in year " + int(student1.Graduation_Year)) # ---> This Doesnt works Graduation_Year is already and Int 

# print("Name of the student1 is " + student1.NAME + "Will Graduate in year " + (student1.Graduation_Year)) 
# ---> This Doesnt Work as Graduation Year is int while Everything else in this print statement is a string  AND Because you are tyring to add a string to an Interger   


# print(f"Name of the student1 is {student1.NAME} Will Graduate in year {student.Graduation_Year}") # ---> This works MOST RECOMMENDED


print(f"My graduating year of {student.Graduation_Year} has {student.Number_of_Students} Number of students \n {student1.NAME} \n {student2.NAME}\n {student3.NAME} \n {student4.NAME}")

