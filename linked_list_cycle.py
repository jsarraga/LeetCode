# Approach: 
# 1. Traverse the linked list, and if we've come across a node we've seen before we can assume it has a cyle.
#    Approach works if you're able to modify the linked list.

# Better Approach:
# 2. Imagine the linked list as a race track. If we have two pointers, one going faster than the other, if the
#    faster one 'laps' the slower pointer or collides with the slower pointer, then we know we have a cycle.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # handle for edge case
        if head == None:
            return False

        # we can't start both pointers off at the same point, bc our while loop will return True immediately
        slow = head
        fast = head.next
        
        # handle for fast.next not being not None, so we'll have to make sure it exists
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # if they're the same value, or collide, then we'll return True
            if slow == fast:
                return True
        
        return False
