# So everything in Python is a Method. Like the arthematic operetors, Comaprision operators and all.
# Theres always a Dunder Method Running in the Background. 
# For example: str1 + str2 (Here you can write it as "str1.__add__(str2)"  as well and + does Nothign but call add method)
# So there are built in methods, But you can create your own and Use them for your liking. 


class Counter: 
    def __init__(self):
            self.value = 1
            self.value += 1
            # print(self.value)


    def Count_Up(self):
            self.value += 1


Count1 = Counter()
Count2 = Counter()


Count1 += 1

print(Count1)

                      