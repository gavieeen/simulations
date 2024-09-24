# Pleasant Pairs
import time


def pleasantPairs(arr):
    count = 0
    n2 = len(arr) * 2
    pair_map = {}
    for i, num in enumerate(arr, 1):
        count += pair_map.get((num, i), 0)
        m = (i + i + 1) // num
        while num * m <= n2:
            if m not in pair_map:
                pair_map[(m, num * m - i)] = 0
            pair_map[(m, num * m - i)] += 1
            m += 1
    return count


def pleasant_pairs_n2(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] * arr[j]) == (i + j + 2):
                count += 1
    return count


test = [3, 1]
t1 = time.time()
pleasantPairs(test)  # 1
t2 = time.time()
pleasant_pairs_n2(test)  # 1
print(f"brute force approach: {time.time() - t2}")
print(f"hashmap approach: {t2 - t1}")

test = [6, 1, 5]
t1 = time.time()
pleasantPairs(test)  # 1
t2 = time.time()
pleasant_pairs_n2(test)  # 1
print(f"brute force approach: {time.time() - t2}")
print(f"hashmap approach: {t2 - t1}")

test = [3, 1, 5, 9, 2]
t1 = time.time()
pleasantPairs(test)  # 3
t2 = time.time()
pleasant_pairs_n2(test)  # 3
print(f"brute force approach: {time.time() - t2}")
print(f"hashmap approach: {t2 - t1}")

test = [1, 3, 6, 3, 2, 5, 2, 6, 3, 4, 6, 2, 1, 3, 6, 3, 2, 5, 2, 6, 3, 4, 6, 2]
t1 = time.time()
pleasantPairs(test)  # 3
t2 = time.time()
pleasant_pairs_n2(test)  # 3
print(f"brute force approach: {time.time() - t2}")
print(f"hashmap approach: {t2 - t1}")
