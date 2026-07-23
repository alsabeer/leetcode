# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = None
        temp = head      
        t = head         

        while temp and temp.next:
            temp = temp.next.next
            new = t.next
            t.next = p
            p = t
            t = new
        if temp:
            t = t.next
        while p and t:
            if p.val != t.val:
                return False
            p = p.next
            t = t.next

        return True