# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # the time complexity of the following code is O(m+n) while m and n are the length of the list 1 and the list 2. The space complexity is O(1) because we are just creating a extra dummy node and then rearranging the other nodes in the list
        dummy_node = ListNode()
        dummy_node.next = None
        curr = dummy_node
        l1 = list1
        l2 = list2

        while l1 and l2 :
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        while l1:
            curr.next = l1
            l1 = l1.next
            curr = curr.next
        
        while l2:
            curr.next = l2
            l2 = l2.next
            curr = curr.next
        
        curr.next = None

        return dummy_node.next

        