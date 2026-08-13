# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # this is a simple one, wht you can do is that count all the elements and then remvoe the target element in the second run so the time complexity becomes O(2n)
        # following is the code to the above approach
        count = 0

        curr = head

        while curr:
            count+=1
            curr = curr.next
        
        dummy = ListNode()
        dummy.next = head
        target = count - n 

        curr = dummy
        curr_count = 0
        while curr_count != target:
            curr = curr.next
            curr_count += 1

        curr.next = curr.next.next 

        return dummy.next