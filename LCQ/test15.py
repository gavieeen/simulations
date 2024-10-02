import time
import random

# Sum-based method to find the missing number
def find_missing_sum_method(arr):
    first_val = arr[0]
    last_val = arr[-1]
    
    # Calculate the expected sum of the range using arithmetic series formula
    expected_sum = (first_val + last_val) * (last_val - first_val + 1) // 2
    
    # Actual sum of the array
    actual_sum = sum(arr)
    
    # The missing value is the difference
    return expected_sum - actual_sum

# Binary search method to find the missing number
def find_missing_binary_search(arr):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Check the difference between arr[mid] and the index
        if arr[mid] != arr[0] + mid:  # If difference suggests missing element
            right = mid - 1
        else:
            left = mid + 1
    
    # The missing value is arr[0] + left (since left will point to the location where the number should be)
    return arr[0] + left

# Helper function to generate test cases
def generate_test_case(size):
    arr = list(range(1, size + 1))  # Create a sorted list from 1 to size
    missing_value = random.randint(2, size - 1)  # Random missing value, but not first or last
    arr.remove(missing_value)  # Remove the missing value
    return arr, missing_value

# Test performance on 10^5 test cases
def test_performance():
    num_tests = 10**5
    size = 1000  # Example array size for each test case

    # Generate test cases
    test_cases = [generate_test_case(size) for _ in range(num_tests)]

    # Time the sum-based method
    start_time = time.time()
    for arr, _ in test_cases:
        find_missing_sum_method(arr)
    sum_method_time = time.time() - start_time

    # Time the binary search method
    start_time = time.time()
    for arr, _ in test_cases:
        find_missing_binary_search(arr)
    binary_search_time = time.time() - start_time

    print(f"Sum-based method time for {num_tests} test cases: {sum_method_time:.6f} seconds")
    print(f"Binary search method time for {num_tests} test cases: {binary_search_time:.6f} seconds")


# Run performance test
if __name__ == "__main__":
    test_performance()
