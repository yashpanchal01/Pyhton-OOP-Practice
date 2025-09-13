# Magic Methods = Created using dunder Used to Compare Objects (=, <, >)




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
