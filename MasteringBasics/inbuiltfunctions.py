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

x = 'AABCAADDD'
k = 3

def merge_the_tools(string, k):
    for i in range(0, len(string), k):  # For first iteration i = 0, second i = 3, then 6    as k = 3 Runs till len(string) iterations
        substring = string[i : i+k] 
        print(i)
        print(substring)

        unique_chars = "".join(dict.fromkeys(substring))
        
        # 3. Print the result for that chunk
        print(unique_chars)


merge_the_tools(x, k)
    
# def print_something():
#     print("Hellow world!")

# print(f"{print_something()}")