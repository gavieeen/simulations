import time

# Function using modulo operation
def mod_test(n):
    return (n // 10) % 2 == 1

# Function using bitwise AND operation
def and_test(n):
    return ((n // 10) & 1) == 1

# Testing time for modulo operation
start_time_mod = time.time()
for i in range(1, 100000001):
    mod_test(i)
end_time_mod = time.time()

# Testing time for bitwise AND operation
start_time_and = time.time()
for i in range(1, 100000001):
    and_test(i)
end_time_and = time.time()

# Calculating and printing the times
mod_time = end_time_mod - start_time_mod
and_time = end_time_and - start_time_and

print(f"Time taken by modulo operation: {mod_time:.6f} seconds")
print(f"Time taken by bitwise AND operation: {and_time:.6f} seconds")