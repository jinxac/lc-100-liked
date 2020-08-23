# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def movePointer(self, head, diff):
        while diff > 0:
            head = head.next
            diff -= 1
    
        return head 
    
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:        
        lenA = 0
        lenB = 0
        tempA = headA
        tempB = headB
        
        while tempA or tempB:
            if tempA:
                lenA += 1
                tempA = tempA.next
            if tempB:
                lenB+= 1
                tempB = tempB.next        
            
            
        diff = lenA - lenB
        
        if diff > 0:
            headA = self.movePointer(headA, diff)
        else:
            headB = self.movePointer(headB, abs(diff))
            
        
        while headA and headB:
            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        
        return None
