import time
import random
import string

# Compare performance of `==` vs `is` operators

def generate_test_array(length=10000):
    arr = []
    for i in range(length):
        if i % 2 == 0: arr.append("*")
        else: arr.append(random.choice(string.ascii_letters))
    return arr

# Function using `x == "*"`
def test_equals_operator(arr):
    for x in arr:
        if x == "*":
            pass

# Function using `x is "*"`
def test_is_operator(arr):
    for x in arr:
        if x is "*":
            pass

# Function to calculate the average time of execution
def average_time(func, arr, trials=10):
    total_time = 0
    for _ in range(trials):
        start_time = time.time()
        func(arr)
        total_time += time.time() - start_time
    return total_time / trials

# Generate the test array
test_array = generate_test_array()

# Compare the two functions
avg_time_equals = average_time(test_equals_operator, test_array)
avg_time_is = average_time(test_is_operator, test_array)

print(f"Average time using '==': {avg_time_equals:.8f} seconds")
print(f"Average time using 'is': {avg_time_is:.8f} seconds")

# Average time using '==': 0.00011270 seconds
# Average time using 'is': 0.00011520 seconds