"""import heapq

# A priority queue is just a list that we manage with heapq
# We'll use tuples where the first item is the priority
# (lower number = higher priority)
tasks = []

# Insert items with their priorities
heapq.heappush(tasks, (2, 'Do laundry'))
heapq.heappush(tasks, (1, 'Pay bills')) # Highest priority
heapq.heappush(tasks, (3, 'Wash car'))
heapq.heappush(tasks, (2, 'Buy groceries'))

print(f"Current tasks in heap order: {tasks}")

# Process tasks by extracting the highest priority item first
print("\nProcessing tasks...")
while tasks:
    # heappop always removes and returns the smallest item
    print(tasks)
    priority, task_name = heapq.heappop(tasks)

    print(f"Processing task: '{task_name}' with priority {priority}")

"""

x = [(1, 2), (3, 4)]
i, j = x 
print(f"this is i : {i}, this is j : {j}")