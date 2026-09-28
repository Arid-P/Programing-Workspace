from collections import deque

# Creating a deque
d = deque([1, 2, 3, 4])
print("Initial deque:", d)

# Adding elements to both ends
d.append(5)       # Adds 5 to the right side
d.appendleft(0)   # Adds 0 to the left side
print("Deque after appending:", d)

# Removing elements from both ends
d.pop()           # Removes 5 from the right side
d.popleft()       # Removes 0 from the left side
print("Deque after popping:", d)

# Rotating the deque (useful in certain sliding window scenarios)
d.rotate(1)       # Rotates elements to the right
print("Deque after rotation:", d)
d.rotate(-1)      # Rotates elements to the left
print("Deque after reverse rotation:", d)

# Using deque as a queue (FIFO)
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue before dequeuing:", queue)
queue.popleft()   # Dequeue operation
print("Queue after dequeuing:", queue)

# Using deque as a stack (LIFO)
stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack before popping:", stack)
stack.pop()       # Pop operation
print("Stack after popping:", stack)