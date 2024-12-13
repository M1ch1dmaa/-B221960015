class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base case
        if len(nums) < 3: return max(nums)
        # M(emory) stores maximum money until last two points
        M = nums[0], max(nums[0], nums[1])
        # We iterate M until we get the max money in the last house
        for i in range(2, len(nums)):
            # Only store last two points to save memory
            M = M[1], max(nums[i]+M[0], M[1])
        return M[1]
