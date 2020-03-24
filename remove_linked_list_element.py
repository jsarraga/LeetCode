# Approach:
#   One pointer solution. Have a pointer act as a dummy head and traverse the list.
#   If the pointer finds the target val, we just change ptr.next to ptr.next.next and skip the target val


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # make a dummy head that is a node not actually part of the list
        dummy_head = ListNode(-1)
        # the dummy head is a node that starts before the actual linked list
        dummy_head.next = head
        # pointer used to traverse the list
        current_node = dummy_head

        # while there actually is a next node, we start the while loop
        while current_node.next != None:
            # if the next value is the target value, we skip it
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                # otherwise move the current node to the next one to continre traversing
                current_node = current_node.next
        
        return dummy_head.next