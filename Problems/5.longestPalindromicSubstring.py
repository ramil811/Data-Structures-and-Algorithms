class Solution(object):
    def isPalindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s):
        if self.isPalindrome(s):
            return s

        charIndexes = {}
        palindromeString = ""
        stack = None
        for index, char in enumerate(s):
            if (char not in charIndexes):
                charIndexes[char] = [index]
            else:
                charIndexes[char].append(index)
                for charIndex in charIndexes[char]:
                    stringToCheck = s[charIndex:index+1]
                    if (self.isPalindrome(stringToCheck) and len(stringToCheck) > len(palindromeString)):
                        palindromeString = stringToCheck

        return s[0] if palindromeString == "" else palindromeString

if __name__ == '__main__':
    # create the string
    s = "babad"
    print(Solution().longestPalindrome(s))

    s = "cbbd"
    print(Solution().longestPalindrome(s))

    s = "a"
    print(Solution().longestPalindrome(s))

    s = "ac"
    print(Solution().longestPalindrome(s))