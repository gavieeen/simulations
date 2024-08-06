from math import ceil

arr1 = [2, 3, 6, 7]
arr2 = [2, 4, 5, 7]
arr3 = [2, 4, 6, 7]
arr4 = [3, 4, 4, 7]

arrs = [arr1, arr2, arr3, arr4]

for arr in arrs:
    cost = 0
    maxx = arr[-1]
    for i in range(len(arr) - 1):
        minn = arr[i]
        cost += ceil((minn + maxx) / (maxx - minn + 1))
        maxx += minn
    print(cost)
    
    total_sum = sum(arr)
    max_val = max(arr)
    length = len(arr)
    
    print(ceil(total_sum / length) + max_val)
