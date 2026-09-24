class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set(nums)
        numSetLen = len(numSet)
        numsLen = len(nums) 
        if numSetLen == numsLen:
            return False
        else:
            return True
