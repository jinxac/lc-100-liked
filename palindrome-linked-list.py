# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def array_approach(self, head):
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        i = 0
        j = len(arr) - 1
        
        while i < j:
            if arr[i] != arr[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def isPalindrome(self, head: ListNode) -> bool:
        # return self.array_approach(head)
        return self.list_split_reverse_approach(head)
        
