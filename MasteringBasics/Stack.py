My_stack = []
print(len(My_stack) == 0) # isEmpty ? 
My_stack.append(1)
print(My_stack)
My_stack.pop(0) # Pop(index)

# My_stack.append(1)
print(My_stack)
try: 
    print(My_stack[-1]) # Peek at last element 
except: 
    print("Empty stack")
print(len(My_stack)) # Size