class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        # Initialize the first two steps
        first, second = 1, 2

        # Calculate the number of ways to reach each step
        for i in range(3, n + 1):
            first, second = second, first + second

        return second
    
if __name__ == '__main__':
    n = 5
    print(Solution().climbStairs(n))  # Output: 8

    n = 10
    print(Solution().climbStairs(n))  # Output: 89

    n = 1
    print(Solution().climbStairs(n))  # Output: 1

    n = 2
    print(Solution().climbStairs(n))  # Output: 2

    n = 3
    print(Solution().climbStairs(n))  # Output: 3