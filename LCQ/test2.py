import timeit

# Sample list
lst = [1, 2, 3, 1, 2, 1, 4, 5, 1, 6] * 1000

# Time the count() function
count_time = timeit.timeit(lambda: lst.count(1), number=1000)
print(f"count() time: {count_time:.6f} seconds")

# Time the sum() function
sum_time = timeit.timeit(lambda: sum(lst), number=1000)
print(f"sum() time: {sum_time:.6f} seconds")

# count() time: 0.044671 seconds
# sum() time: 0.026098 seconds