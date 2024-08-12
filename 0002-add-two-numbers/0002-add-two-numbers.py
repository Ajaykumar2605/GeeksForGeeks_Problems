# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode()  # Dummy node to simplify the code
        current = dummy
        
        while l1 or l2 or carry:
            # Calculate the sum of current digits and carry
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            # Update carry
            carry = total // 10
            
            # Create a new node with the digit sum
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next