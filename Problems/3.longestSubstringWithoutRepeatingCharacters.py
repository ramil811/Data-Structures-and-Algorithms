class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # create a dictionary to store the character and its index
        bag = {}

        # initialize the start and max length
        start = 0
        longest = 0

        # iterate through the string
        for right, char in enumerate(s):
            # check if the character is in the dictionary
            if char in bag:
                # update the start
                start = max(start, bag[char] + 1)

            # update the character index
            bag[char] = right

            # update the longest substring
            longest = max(longest, right - start + 1)

        return longest
    

if __name__ == '__main__':
    # create the string
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(Solution().lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))