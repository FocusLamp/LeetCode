        # Medium Difficulty O(n) O(n)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack = []
        
        while current:
            while stack and stack[-1].val < current.val:
                stack.pop()
            stack.append(current)
            current = current.next
        
        previous_node = None
        while stack:
            current = stack.pop()
            current.next = previous_node
            previous_node = current
        
        return current
