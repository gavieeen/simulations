from math import ceil

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
print(feas(execution, x, y, 4))
print()
print(feas(execution, x, y, 3))
print()
print(feas(execution, x, y, 2))

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