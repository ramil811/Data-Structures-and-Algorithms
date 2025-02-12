class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # initialize the max area to 0
        max_area = 0

        # initialize the left and right pointers
        left = 0
        right = len(height) - 1

        # loop through the height list
        while left < right:
            # calculate the area
            area = min(height[left], height[right]) * (right - left)

            # update the max area
            max_area = max(max_area, area)

            # move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        # return the max area
        return max_area
        

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height)) # 49

    height = [1,1]
    print(Solution().maxArea(height)) # 1

    height = [4,3,2,1,4]
    print(Solution().maxArea(height)) # 16

    height = [1,2,1]
    print(Solution().maxArea(height)) # 2