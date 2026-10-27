class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {
            ']' : '[',
            ')' : '(',
            '}' : '{'
        }

        for char in s: 
            if char in '({[':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                top = stack.pop() #top element of stack 

                if top != matching[char]:
                    return False
        
        return len(stack) == 0