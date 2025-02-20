# Nathan Amazon Interview Question
"""
Given array, find all indices a, b, c, d s.t.
- a < b < c < d
- array[a] + array[b] + array[c] = array[d]
"""

from collections import defaultdict

def find_quadruples_brute(nums):
    n = len(nums)
    quadruples = 0
    
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        quadruples += 1
    
    return quadruples

def find_quadruples_optim(nums):
    # rearrange equation to nums[a] + nums[b] = -nums[c] + nums[d]
    n = len(nums)
    quadruples = 0
    ab_sum = defaultdict(int)
    
    for c in range(2, n - 1):
        b = c - 1
        for a in range(b):
            ab_sum[nums[a] + nums[b]] += 1
            
        for d in range(c + 1, n):
            quadruples += ab_sum[-nums[c] + nums[d]]
    
    return quadruples

tests = [
    [1, 1, 3, 3, 5],
    [2, 2, 8, 2, 10],
    [1, 1, 1, 3, 3, 5]
]

for t in tests:
    true, test = find_quadruples_brute(t), find_quadruples_optim(t)
    print(f'{t = }')
    if true != test:
        print(f'{true = }, {test = }')
    else:
        print(f'Quadruples found: {test}')