class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # ignore leading whitespace
        s = s.lstrip()
        
        # check for empty string
        if s == "":
            return 0

        # sign
        sign = 1 if s[0] != '-' else -1
        s = s[1:] if s[0] in ['-', '+'] else s

        # conversion
        result = 0
        for digit in s:
            if digit.isdigit():
                result = result * 10 + int(digit)
            else:
                break

        # check for 32-bit overflow
        if result > 2**31 - 1:
            result = 2**31 - 1 if sign == 1 else 2**31

        return sign * result
        
    
if __name__ == '__main__':
    s = "42"
    print(Solution().myAtoi(s))
    s = "   -42"
    print(Solution().myAtoi(s))
    s = "4193 with words"
    print(Solution().myAtoi(s))
    s = "1337c0d3"
    print(Solution().myAtoi(s))