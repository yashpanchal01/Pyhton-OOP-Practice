# Enter your code here. Read input from STDIN. Print output to STDOUT



n_m = list(input().split(" "))
Uni = list(set(input().split(" ")))
set_A = list(set(input().split(" "))) # Elements of A 
set_B = list(set(input().split(" ")))# Elements of B 

n = int(n_m[0])
m = int(n_m[1])
print(n_m)
print(Uni)
print(set_A)
print(set_B)

# m = list1[1]
# n = len(list2)

Happiness = 0
for i in range(n):
    i = Uni[i]
    print(f"i : {i}")
    for x in range(m):
        print(f"x:  {x}")
        if i == set_A[x]:
            Happiness += 1
        elif i == set_B[x]:
            Happiness -= 1

print(Happiness, ": This is Happiness")

