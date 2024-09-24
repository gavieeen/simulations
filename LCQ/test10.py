from math import ceil
import heapq

def feas(execution, x, y, operations):
    diff = x - y
    for el in execution:
        print(f'before el {operations = }')
        adj = max(0, el - operations*y)
        print(f'{adj = }')
        operations -= ceil(adj / diff)
        print(f'after el {operations = }')
        if operations < 0:
            return False
    return True

def minTimeToExecute(execution, x, y):
    n = len(execution)
    l, r = 0, sum(execution)
    ret = -1
    while l <= r:
        m = (l + r) // 2
        if feas(execution, x, y, m):
            ret = m
            r = m - 1
        else:
            l = m + 1
            
    return ret

# Time: O(n * log(sum(execution)))
execution = [3,4,1,7,6]
x, y = 6, 1

# Binary search on operations = 3 for [3,4,1,7,6], x=6, y=1:
# diff = 5
# adj = max(0, 3 - 3 * 1) = 0
# operations -= ceil(0 / diff) = 3
# adj = max(0, 4 - 3 * 1) = 1
# operations -= ceil(1 / diff) = 2
# adj = max(0, 0 - 2 * 1) = 0
# operations -= ceil(0 / diff) = 2
# adj = max(0, 7 - 2 * 1) = 5
# operations -= ceil(5 / diff) = 1
# adj = max(0, 6 - 1 * 1) = 5
# operations -= ceil(5 / diff) = 0
# operations >= 0 -> True

from collections import Counter

def solve_problem1(n: int, user_events: list[int]) -> int:
    def remove_old_freq(old_freq: int) -> bool:
        if old_freq == 0:
            return False

        seen_freqs[old_freq] -= 1
        if seen_freqs[old_freq] == 0:
            del seen_freqs[old_freq]
            return True
        return False

    def add_new_freq(new_freq: int) -> bool:
        if new_freq == 0:
            return False

        seen_freqs[new_freq] += 1
        return seen_freqs[new_freq] == 1

    freq = Counter(user_events)
    min_freq = [] # min heap for min freq
    left = 0
    counting_dict = Counter()
    seen_freqs = Counter()
    ans = n if n <= 2 else 2

    for right, num in enumerate(user_events):
        # remove old frequency
        remove_old_freq(counting_dict[num])

        # update new frequency
        counting_dict[num] += 1
        if add_new_freq(counting_dict[num]):
            heapq.heappush(min_freq, (freq[num], num))

        while min_freq and counting_dict[num] > min_freq[0][0]: # condition needs to be adjusted
            old_freq = counting_dict[user_events[left]]
            
            # remove the old frequency of the number currently at i=left
            if counting_dict[user_events[left]] == min_freq[0][1] and remove_old_freq(old_freq):
                heapq.heappop(min_freq)
            
            # update the new frequency when moving the left pointer
            add_new_freq(old_freq - 1)
            counting_dict[user_events[left]] -= 1
            freq[user_events[left]] -= 1
            
            # move the left pointer
            left += 1
        
        # only one frequency is observed
        if len(seen_freqs) == 1:
            ans = max(ans, right - left + 1)

    return ans
    
user_events = [3,1,1,3,9,9,9,9,9,9,9]
print(solve_problem1(4, user_events))
user_events = [1,2,1,3,4,2,4,3,3,4]
print(solve_problem1(10, user_events))
user_events = [3,9,9,9,1,9,9,9,9]
print(solve_problem1(len(user_events), user_events))