'''students = [['harry', 23.0], ['mon', 25.0], ['bro', 27.0], ['code', 25.00]]

set_scores = list(set(students[i][1] for i in range(len(students))))
set_scores.sort()

list_second_lowers = []
for i in range(len(students)): 
    if students[i][1] == set_scores[-2]:
        x = students[i][0]
        list_second_lowers.append(x)

list_second_lowers.sort()

print("\n".join(list_second_lowers))



'''

# string = 'AABCAADDD'
# k = 3

def merge_the_tools(string, k):
    list1 = []
    list1.append(string for i in range(k+1))
    list2 = list(set(list1))
    x = "".join(list2)

    print(x, end="\n")

print(f"{merge_the_tools('AABCAADDD', 3)}")

# def print_something():
#     print("Hellow world!")

# print(f"{print_something()}")