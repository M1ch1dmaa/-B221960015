def threeSum(nums):
    result = set()
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet to handle duplicates
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    
    return list(result)

nums1 = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums1))

nums2 = [0, 1, 1]
print(threeSum(nums2))

nums3 = [0, 0, 0]
