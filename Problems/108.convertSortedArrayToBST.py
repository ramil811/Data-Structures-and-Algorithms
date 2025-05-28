class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Convert a sorted array to a height-balanced binary search tree.
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    nums = [-10, -3, 0, 5, 9]
    bst_root = solution.sortedArrayToBST(nums)
    
    # Function to print the tree in-order for verification
    def print_in_order(node):
        if node:
            print_in_order(node.left)
            print(node.val, end=' ')
            print_in_order(node.right)

    print_in_order(bst_root)  # Output: -10 -3 0 5 9
    print()  # For better readability in output