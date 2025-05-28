class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                openingBracket = stack.pop()
                if char == ')' and openingBracket != '(':
                    return False
                if char == ']' and openingBracket != '[':
                    return False
                if char == '}' and openingBracket != '{':
                    return False
        
        return True if len(stack) == 0 else False
        

if __name__ == "__main__":
    s = "()"
    print(f's: {s}, isValid: {Solution().isValid(s)}')

    s = "()[]{}"
    print(f's: {s}, isValid: {Solution().isValid(s)}')

    s = "(]"
    print(f's: {s}, isValid: {Solution().isValid(s)}')

    s = "([])"
    print(f's: {s}, isValid: {Solution().isValid(s)}')
