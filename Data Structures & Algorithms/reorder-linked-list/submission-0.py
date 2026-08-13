# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # get the pointers
        second = slow.next # start of the 2nd list
        slow.next = None # breaking the initial link
        prev = None # for reversing the second part 
        
        # reverse the 2nd half 
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge the 2 halfs
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
