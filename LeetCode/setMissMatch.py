def findErrorNums(nums):
    nums.sort()
    missing = None
    for key, val in enumerate(nums):
        # print(key, val)
        # print(nums[abs(val)-1])
        if abs(nums[key]) - 1 != key:
            missing = key + 1
        if nums[abs(val)-1] < 0:
            return [abs(val), missing]
        nums[abs(val)-1] = -nums[abs(val)-1]
    return []



#print(findErrorNums([1,2,2,4]))
print(findErrorNums([3,2,2]))