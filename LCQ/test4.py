import time
from collections import deque

n = 1000000

start_time = time.time()
stack = []
for i in range(n):
    stack.append(i)
stack.reverse()
end_time = time.time()
print(f"List (stack) append and reverse: {end_time - start_time} seconds")

start_time = time.time()
dq = deque()
for i in range(n):
    dq.appendleft(i)
end_time = time.time()
print(f"Deque appendleft: {end_time - start_time} seconds")
