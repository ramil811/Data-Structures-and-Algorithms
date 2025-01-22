class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # create a dictionary to store the number and its index
        num_index = {}

        # iterate through the list
        for index, num in enumerate(nums):
            # calculate the difference
            diff = target - num

            # check if the difference is in the dictionary
            if diff in num_index:
                return [num_index[diff], index]

            # add the number to the dictionary
            num_index[num] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(Solution().twoSum(nums, target))