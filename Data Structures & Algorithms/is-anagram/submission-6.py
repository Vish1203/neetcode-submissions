class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False 

        charCount = {}

        for char in s: 
            charCount[char] = charCount.get(char, 0) + 1
        for char in t: 
            charCount[char] = charCount.get(char, 0) - 1
        
        return all(value == 0 for value in charCount.values())