class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False 

        charCount = {}

        for char in s: 
            if char not in charCount:
                charCount[char] = 1
            else:
                charCount[char] += 1
        
        for c in t: 
            if c not in charCount:
                return False
            else:
                charCount[c] -= 1
        
        return all(value == 0 for value in charCount.values())