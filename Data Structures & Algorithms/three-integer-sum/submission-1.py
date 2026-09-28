class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) 
        # O(1)
        result = []
        
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: 
                # checks for duplicates in a sorted list
                continue
            a = nums[i]
            left = i + 1 
            right = len(nums) - 1
            while left < right: 
                total = a + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else: 
                    threeSum = [a, nums[left], nums[right]]
                    if threeSum not in result: 
                        result.append(threeSum)
                    left += 1
                    right -= 1
        return result

