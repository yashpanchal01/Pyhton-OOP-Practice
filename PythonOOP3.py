# Duck Typing = is an another way of achieving polymorphism besides using inheritance 
#                 objects must have the minimum nessesary attributes/Methods.
#                 "If it looks like a duck, qauks like a duck it must be a duck"
# Basically meaning we will Name the Methodes and attributes or Variables of One class to match another class's Methods or Variables 
# Because They are similar, in attributes or in some way. RIGHT ? 



# INSTANT METHODS and STATIC METHODS DIFFERENCE ===> Clear ? 

# @something ---> this is called a decorator  Ex: @staticmethod ---> this is a decorator used when creating a static method

class Employee: 
    def __init__(self, Name, Position):
        self.Name = Name
        self.Position = Position

    def get_info(self):
        return f"{self.Name} is Employee with position {self.Position}"
    
    @staticmethod
    def is_a_Valid_poisiton(position):
        Positions = ["Manager", "Cook", "Helper", "Fresher"]
        return position in Positions 

Employee1 = Employee("YASH", "Manager")

# print(Employee1.Name)
print(f"{Employee1.Name} is at Employee Position = {Employee1.Position}, which is a Valid Position = {Employee.is_a_Valid_poisiton(Employee1.Position)}")
# print(Employee.is_a_Valid_poisiton("Astronaut"))

