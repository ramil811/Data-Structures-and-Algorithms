class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getHeight(self, node):
        """
        Helper function to get the height of a node.
        :type node: TreeNode
        :rtype: int
        """
        if not node:
            return -1
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def insertIntoBST(self, root, val):
        """
        Helper function to insert a value into the BST.
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if val < root.val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                root.left = self.insertIntoBST(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                root.right = self.insertIntoBST(root.right, val)

        # Check the balance factor
        balance = self.getHeight(root.left) - self.getHeight(root.right)
        # print(f"Inserting {val}: Node {root.val} has balance factor {balance}")
        if balance > 1:
            # print(f"Node {root.val} is left heavy")
            # self.printTree(root)
            # Left heavy
            if val < root.left.val:
                # Left Left Case
                return self.rightRotate(root)
            else:
                # Left Right Case
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balance < -1:
            # print(f"Node {root.val} is right heavy")
            # self.printTree(root)
            # Right heavy
            if val > root.right.val:
                # Right Right Case
                return self.leftRotate(root)
            else:
                # Right Left Case
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
            
    def leftRotate(self, z):
        """
        Helper function to perform left rotation.
        :type z: TreeNode
        :rtype: TreeNode
        """
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        return y
    
    def rightRotate(self, z):
        """
        Helper function to perform right rotation.
        :type z: TreeNode
        :rtype: TreeNode
        """
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        return y

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        root = TreeNode(nums[0])

        for num in nums[1:]:
            root = self.insertIntoBST(root, num)

        return root
    
    def printTree(self, node):
        """
        Helper function to print the tree in-order.
        Performs an in-order traversal and prints the values.
        :type node: TreeNode
        :rtype: None
        """
        if node:
            # print(node.left, node.val, node.right)
            self.printTree(node.left)
            print(node.val, end=' ')
            self.printTree(node.right)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    bst = Solution().sortedArrayToBST(nums)
    # Solution().printTree(bst)  # Output: -10 -3 0 5 9
    # print()  # For better readability of output

    nums = [1, 2, 3, 4, 5, 6, 7]
    bst = Solution().sortedArrayToBST(nums)
    # Solution().printTree(bst)  # Output: 1 2 3 4 5 6 7
    # print()  # For better readability of output