def removeElement(self, nums: List[int], val: int) -> int:
    first, second = 0, 0
    
    while second < len(nums):
        if nums[second] != val:
            nums[first], nums[second] = nums[second], nums[first]
            first += 1
        second += 1
    return first

if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement(nums, val))

    nums = [1]
    val = 1
    print(removeElement(nums, val))
