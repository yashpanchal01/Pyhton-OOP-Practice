# When to use OBJECTS and Classes ? 
# Whenever There are Objects in Context, Such as Phone, book, Cup
# Attributes(Variables) are Properties/Parameters of Objects -> For a Phone => Model_Number = 12091314, Turned_On = True, Price = 50krs.
# Methods(Functions) are Functions That belong to and Object, Methods = Functions  -> For a Phone, Def Make_call():
#  Def Recive_call(): Def Turn_on                 
#
#                    For a cup => Attributes: Is_empty, Temprature, Liquid
#                                   Methodes: def Empty_cup, Def Fill_cup, Def Throw_cup_in_Trash_can
#
# Constructor is a special Type of Method. 

class car:
    def __init__(self, Model_Number, Color, Price, Brand, Sports):
        self.Model_Number = Model_Number
        self.Color = Color
        self.Price = Price 
        self.Brand = Brand
        self.Sports = Sports

car1 = car(123456, "Blue", 4000000, "Porche", True)
car2 = car(987654, "Yellow", 300000, "Mustang", True)
car3 = car(798998, "Red", 700000, "Corvette", False  )



print(car3.Model_Number)
print(car3.Brand)
print(car3.Price)
print(car3.Color)
print("----------------------\n")

print(car2.Model_Number)
print(car2.Brand)
print(car2.Price)
print(car2.Color)
print("----------------------\n")

print(car1.Model_Number)
print(car1.Brand)
print(car1.Price)
print(car1.Color)
