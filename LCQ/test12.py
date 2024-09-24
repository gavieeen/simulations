test = [3,3,4,7,8]
k = 5

def findTriplesDivisibleByK(nums, k):
    count = 0
    n = len(test)
    nums = [num % k for num in nums]
    for i, num in enumerate(nums):
        rmod = {}
        for j in range(i+1, n):
            if nums[j] in rmod:
                count += rmod[nums[j]]
            rmod[(k - ((num + nums[j]) % k))] = rmod.get((k - ((num + nums[j]) % k)), 0) + 1
    return count

print(findTriplesDivisibleByK(test, k)) # 3
test = [1,2,3,4,5]
print(findTriplesDivisibleByK(test, k)) # 0