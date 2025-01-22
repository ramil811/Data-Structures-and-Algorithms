class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)

        return string == string[::-1]
    
if __name__ == '__main__':
    x = 121
    print(Solution().isPalindrome(x))

    x = -121
    print(Solution().isPalindrome(x))

    x = 10
    print(Solution().isPalindrome(x))