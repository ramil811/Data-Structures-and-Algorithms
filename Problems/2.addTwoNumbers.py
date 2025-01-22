class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: Optional[ListNode]
        """

        # to store carry for the next digit
        carryForward = 0

        # create a dummy node
        dummy = ListNode()

        l1Head = l1
        l2Head = l2

        # create a pointer to the dummy node
        currL3 = dummy

        # iterate through the lists
        while l1Head or l2Head or carryForward > 0:
            # get the value of the nodes
            l1Val = l1Head.val if l1Head else 0
            l2Val = l2Head.val if l2Head else 0

            # calculate the sum
            result = l1Val + l2Val + carryForward

            # calculate the carry
            carryForward = result // 10

            # calculate the value of the node
            currL3.next = ListNode(result % 10)

            # move the pointers
            currL3 = currL3.next
            l1Head = l1Head.next if l1Head else None
            l2Head = l2Head.next if l2Head else None

        return dummy.next
    

if __name__ == '__main__':
    # create the first linked list
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    # create the second linked list
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    # add the two linked lists
    result = Solution().addTwoNumbers(l1, l2)

    # print the result
    while result:
        print(result.val, end=' ')
        result = result.next
