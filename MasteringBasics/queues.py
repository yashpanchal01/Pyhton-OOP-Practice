from collections import deque

queue = deque()

# Enqueue elements
queue.append(1)
queue.append(2)
queue.append(3)
print(f"Deque after enqueuing: {queue}")

# Dequeue elements
item = queue.popleft()
print(f"Dequeued item: {item}")
print(f"Deque after dequeuing: {queue}")