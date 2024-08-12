# https://leetcode.com/discuss/interview-question/4031463/Code-Signal-practice-test-question
# Given an array of integers a, return the sum of all a[i] º a[j], where a[i] º a[j] is 
# defined as the concatenation of a[i] and a[j] e.g., if a[0] = 1 and a[i] = 2 then a[i] º a[j] = 12.

# The correct output can be obtained with sum(int(str(ai) + str(aj) for ai in a for aj in a))
# but it is too slow for one of the hidden test cases. Caching str(ai) and str(aj) does not make it fast enough either. 
# Does anyone have a solution that is efficient enough?

import time
import itertools
import random

def method_concat(a):
    return sum(int(str(ai) + str(aj)) for ai in a for aj in a)

def method_append(a):
    n = len(a)
    a_sum = 0
    pow10_of_a = []

    for ai in a:
        pow10_of_a.append(10 ** len(str(ai)))
        a_sum += ai

    return sum(a[i] * pow10_of_a[j] for i in range(n) for j in range(n)) + (a_sum * n)

def method_itertools(a):
    n = len(a)
    a_sum = sum(a)
    pow10_of_a = [10 ** len(str(ai)) for ai in a]
    return sum(ai * pow10_of_a[j] for ai, j in itertools.product(a, range(n))) + (a_sum * n)


def average_time(func, a, trials=10):
    total_time = 0
    for _ in range(trials):
        start_time = time.time()
        func(a)
        total_time += time.time() - start_time
    return total_time / trials

# Generate random inputs
random_inputs = [[random.randint(0, 1000) for _ in range(random.randint(0, 1000))] for _ in range(10)]

# Measure average times for each method
for a in random_inputs:
    avg_time_itertools = average_time(method_itertools, a)
    avg_time_append = average_time(method_append, a)
    avg_time_concat = average_time(method_concat, a)
    
    print(f"Average time for method_itertools for input of length {len(a)} with max value {max(a)}: {avg_time_itertools:.6f} seconds")
    print(f"Average time for method_append for input of length {len(a)} with max value {max(a)}: {avg_time_append:.6f} seconds")
    print(f"Average time for method_concat for input of length {len(a)} with max value {max(a)}: {avg_time_concat:.6f} seconds")
    print("-" * 60)
    
# Average time for method_itertools for input of length 485 with max value 1000: 0.009555 seconds
# Average time for method_append for input of length 485 with max value 1000: 0.009001 seconds
# Average time for method_concat for input of length 485 with max value 1000: 0.043746 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 35 with max value 961: 0.000051 seconds
# Average time for method_append for input of length 35 with max value 961: 0.000051 seconds
# Average time for method_concat for input of length 35 with max value 961: 0.000228 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 44 with max value 995: 0.000077 seconds
# Average time for method_append for input of length 44 with max value 995: 0.000077 seconds
# Average time for method_concat for input of length 44 with max value 995: 0.000377 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 730 with max value 1000: 0.020162 seconds
# Average time for method_append for input of length 730 with max value 1000: 0.021084 seconds
# Average time for method_concat for input of length 730 with max value 1000: 0.107805 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 668 with max value 996: 0.016441 seconds
# Average time for method_append for input of length 668 with max value 996: 0.018538 seconds
# Average time for method_concat for input of length 668 with max value 996: 0.082928 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 406 with max value 997: 0.006173 seconds
# Average time for method_append for input of length 406 with max value 997: 0.006255 seconds
# Average time for method_concat for input of length 406 with max value 997: 0.031062 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 282 with max value 998: 0.002976 seconds
# Average time for method_append for input of length 282 with max value 998: 0.002905 seconds
# Average time for method_concat for input of length 282 with max value 998: 0.014913 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 580 with max value 1000: 0.012571 seconds
# Average time for method_append for input of length 580 with max value 1000: 0.013036 seconds
# Average time for method_concat for input of length 580 with max value 1000: 0.062556 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 94 with max value 993: 0.000334 seconds
# Average time for method_append for input of length 94 with max value 993: 0.000330 seconds
# Average time for method_concat for input of length 94 with max value 993: 0.001698 seconds
# ------------------------------------------------------------
# Average time for method_itertools for input of length 575 with max value 1000: 0.012433 seconds
# Average time for method_append for input of length 575 with max value 1000: 0.013021 seconds
# Average time for method_concat for input of length 575 with max value 1000: 0.062028 seconds
# ------------------------------------------------------------