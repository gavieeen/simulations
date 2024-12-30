import timeit
from typing import List

class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        max_distance = 0
        for i, num in enumerate(nums):
            if i > max_distance: return False
            if i + num > max_distance:
                max_distance = i + num
        return True

    def canJump2(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(goal, -1, -1):
            if i + nums[i] >= goal: goal = i
        return not goal

# Test cases
test_cases = [
    [2, 3, 1, 1, 4],  # Expected True
    [3, 2, 1, 0, 4],  # Expected False
    [2, 0, 0],        # Expected True
    [0],              # Expected True (single element)
    [1, 0, 1, 0],     # Expected False
    [1]*10000,        # Large test case (Expected True)
    [1]*10000 + [0] + [1],  # Large test case (Expected False)
    [1] + [0] + [1]*10000
]

def test_canJump1():
    solution = Solution()
    for case in test_cases:
        solution.canJump1(case)

def test_canJump2():
    solution = Solution()
    for case in test_cases:
        solution.canJump2(case)

if __name__ == "__main__":
    iterations = 1000  # Number of iterations for timing

    time1 = timeit.timeit(test_canJump1, number=iterations)
    time2 = timeit.timeit(test_canJump2, number=iterations)

    print(f"canJump1 time: {time1:.6f} seconds")
    print(f"canJump2 time: {time2:.6f} seconds")
