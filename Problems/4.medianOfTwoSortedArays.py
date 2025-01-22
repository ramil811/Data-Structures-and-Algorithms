class Solution(object):
    def mergeArrays(self, arr1, arr2):
        i = 0
        j = 0

        # create a list to store the merged array
        merged = []

        # iterate through the arrays
        while i < len(arr1) and j < len(arr2):
            # compare the elements
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1

        # add the remaining elements
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge the arrays
        merged = self.mergeArrays(nums1, nums2)

        # calculate the length of the merged array
        mergedLen = len(merged)

        # get the middle index
        mid = mergedLen // 2

        # check if the length is even
        if mergedLen % 2 == 0:
            return (float(merged[mid - 1]) + float(merged[mid])) / 2
        else:
            return float(merged[mid])
        
if __name__ == '__main__':
    # create the arrays
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))