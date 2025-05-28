# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        if not list1 and not list2:
            return None
        
        head1 = list1
        head2 = list2

        result = ListNode(0)
        current = result

        while head1 or head2:
            if not head1:
                current.next = head2
                break
            if not head2:
                current.next = head1
                break
            if head1.val == head2.val:
                current.next = head1
                head1 = head1.next
                current = current.next
                current.next = head2
                head2 = head2.next
            elif head1.val < head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next

        return result.next
    
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(6))))
    list2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(7)))))
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    
    # Print the merged linked list
    current = merged_list
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")