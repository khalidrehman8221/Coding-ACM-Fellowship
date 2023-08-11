# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode()
        dummy.next = head
        fast = dummy
        slow = dummy
        
        
        for _ in range(n + 1):
            fast = fast.next
       
        while fast:
            fast = fast.next
            slow = slow.next
        
        
        slow.next = slow.next.next
        
        return dummy.next