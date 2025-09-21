# Magic Methods = Created using dunder Used to Compare Objects or perform arthmetic operations (=, <, >)




class book: 
    def __init__(self, Name, Author, Pages):
        self.Name = Name
        self.Author = Author 
        self.Pages = Pages

    def __str__(self):
        return f"{self.Name} by {self.Author}"
    
    def __gt__(self, other):
        return self.Pages > other.Pages 
    

book1 = book("Atomic Habbits", "James clear", 340)
book2 = book("Atomic Power", "Mans unclear", 300)
book3 = book("Atomic Orbits", "Maj Yeclear", 250)

print(book1 > book2 and book1 > book3)


# you can only have two 
# Boolean operator is 'and' Not 'AND' 

# Comparisons: __lt__ (<), __gt__ (>), __eq__ (==), __le__ (<=), __ge__ (>=)
# Arithmetic: __add__ (+), __sub__ (-), __mul__ (*), __truediv__ (/)


# The General Rule: 
# A method always takes self as its first argument, followed by whatever other information it needs to do its job.
# This can be zero, one, or multiple additional arguments of any type (integers, strings, lists, or other objects).

