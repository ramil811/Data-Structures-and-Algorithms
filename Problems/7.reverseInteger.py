class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # min and max boundaries
        MAX_32_BIT_INT = 2**31 - 1
        MIN_32_BIT_INT = -2**31

        # using a stack
        stack = []

        # convert int to str
        number = str(x)
        
        # a store for special chars
        prefix = ''

        # iterate through the number char
        for char in number:
            # check if char is an instance of int
            try:
                num = int(char)
                stack.append(char)
            except ValueError as e:
                prefix += char

        print(stack)

        # form return string
        result = prefix

        # pop from the stack
        while len(stack) != 0:
            result += stack.pop()

        print(result)

        result = int(result)

        return 0 if result < MIN_32_BIT_INT or result > MAX_32_BIT_INT else int(result)
    
if __name__ == '__main__':
    # create the string
    x = 123
    print(Solution().reverse(x))

    x = -123
    print(Solution().reverse(x))

    x = 120
    print(Solution().reverse(x))

    x = 0
    print(Solution().reverse(x))