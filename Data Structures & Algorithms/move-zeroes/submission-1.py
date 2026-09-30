class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Time: O(n), Space: O(1)
        left = 0 
        for current in range(len(nums)):
            if nums[current] != 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
    