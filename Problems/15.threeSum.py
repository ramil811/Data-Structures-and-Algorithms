class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        # sort the list
        nums.sort()

        print(f'sorted nums: {nums}')

        # create a set to store the result
        result = set()

        # iterate through the list
        for i in range(len(nums) - 2):
            # create a dictionary to store the complement of the current number
            seen = {}

            # iterate through the list starting from the current index + 1
            for j in range(i + 1, len(nums)):
                # calculate the complement
                complement = -nums[i] - nums[j]

                # if the complement is in the dictionary
                if complement in seen:
                    # add the result to the set
                    result.add((nums[i], nums[j], complement))
                else:
                    # add the current number to the dictionary
                    seen[nums[j]] = j

        # return the set as a list
        return list(result)


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(nums)) # [[-1, -1, 2], [-1, 0, 1]]

    nums = [0, 0, 0]
    print(Solution().threeSum(nums)) # [[0, 0, 0]]

    nums = []
    print(Solution().threeSum(nums)) # []