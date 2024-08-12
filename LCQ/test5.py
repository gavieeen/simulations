import time

# Define the large number
large_number = 10**6

# Measure time for list comprehension
start_time = time.time()
array_comprehension = [0 for _ in range(large_number)]
for i in range(large_number):
    array_comprehension[i] = i
comprehension_time = time.time() - start_time

# Measure time for [0] * large_number
start_time = time.time()
array_zeros = [0] * large_number
for i in range(large_number):
    array_zeros[i] = i
zeros_time = time.time() - start_time

# Measure time for appending to an empty array
start_time = time.time()
array_append = []
for i in range(large_number):
    array_append.append(i)
append_time = time.time() - start_time

# Print the results
print(f"List comprehension time: {comprehension_time} seconds")
print(f"[0] * large_number time: {zeros_time} seconds")
print(f"Appending time: {append_time} seconds")

# Trial 1:
# List comprehension time: 0.0636899471282959 seconds
# [0] * large_number time: 0.0501408576965332 seconds
# Appending time: 0.04095101356506348 seconds

# Trial 2:
# List comprehension time: 0.06090807914733887 seconds
# [0] * large_number time: 0.04341387748718262 seconds
# Appending time: 0.03852963447570801 seconds