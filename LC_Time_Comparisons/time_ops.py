import time
import random

# Generate a list of tests with varying sizes
test_sizes = [random.randint(1, 10**5) for _ in range(10)] + [10**7]
tests = [list(range(size)) for size in test_sizes]

# Define the functions to test
def test_mod(nums):
    result = [num for num in nums if num % 2 == 0]

def test_bitwise_and(nums):
    result = [num for num in nums if num & 1 == 0]

def test_bitwise_shift(nums):
    result = []
    for num in nums:
        num >>= 1
        result.append(num)

def test_floor_division(nums):
    result = []
    for num in nums:
        num //= 2
        result.append(num)
        
def test_pow(nums):
    result = [num ** 2 for num in nums]

def test_mult(nums):
    result = [num * num for num in nums]

# Timing function
def time_function(func, label):
    start_time = time.perf_counter()
    for nums in tests:
        func(nums)
    end_time = time.perf_counter()
    print(f"{label}: {end_time - start_time:.6f} seconds")

# Run tests for all input sizes
print("Odd/Even Check:")
time_function(test_mod, "Using % 2")
time_function(test_bitwise_and, "Using & 1")

# Odd/Even Check:
# Using % 2: 0.466711 seconds
# Using & 1: 0.208935 seconds

print("\nInteger Division:")
time_function(test_bitwise_shift, "Using >>= 1")
time_function(test_floor_division, "Using //= 2")

# Integer Division:
# Using >>= 1: 0.410832 seconds
# Using //= 2: 0.334597 seconds

print("\nSquare:")
time_function(test_pow, "Using **")
time_function(test_mult, "Using *")

# Square:
# Using **: 0.331430 seconds
# Using *: 0.256485 seconds