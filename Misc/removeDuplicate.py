def removeDuplicates(nums):
        ln = len(nums)
        first = 0
        second = 1
        while second < ln:
            while second < ln and nums[first] == nums[second]:
                second += 1
            if second == ln:
                break
            first += 1
            nums[first] = nums[second]
            second += 1
        return first+1


if __name__ == "__main__":
    nums = [1, 1, 1]
    print(removeDuplicates(nums))
    
    nums = [1, 1]
    print(removeDuplicates(nums))

    nums = [1, 1, 2]
    print(removeDuplicates(nums))
    
    nums = [1, 2]
    print(removeDuplicates(nums))