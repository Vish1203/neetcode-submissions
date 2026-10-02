class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1

        for current in range(1, len(nums)):
            if nums[current] != nums[current - 1]:
                nums[left] = nums[current]
                left += 1

        return left 