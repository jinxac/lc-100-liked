# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        
        if not l1 and not l2:
            return None
        
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        
        temp1 = l1
        temp2 = l2
        carry = 0
        
        
        result = ListNode(0)
        temp = result
        
        while temp1 or temp2:
            s = 0
            if temp1:
                s += temp1.val
            if temp2:
                s += temp2.val
                
            s += carry
            
            carry = s // 10
            
            temp.next = ListNode(s % 10)
            
            if temp1:
                temp1 = temp1.next
            
            if temp2:
                temp2 = temp2.next
            
            temp = temp.next
        
            
        if carry:
            temp.next = ListNode(1)
            
        return result.next
