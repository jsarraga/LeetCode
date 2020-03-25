# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # make an instance of a new linked list to return
        head = ListNode(0)
        ptr = head
        
        while True: 
            # handles for both empty lists. head.next is none, so will return an empty list
            if l1 is None and l2 is None:
                break
            # if l1 is a shorter list than l2, we will have the ptr.next point to the remainder of l2's list
            elif l1 is None:
                ptr.next = l2
                break
            # and vice versa
            elif l2 is None:
                ptr.next = l1
                break
            else:
            # need to find out which values of l1 and l2 are smaller, so we create a temporary variable to account for it
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next
            # for the list we will return, we'll create a newnode with the small value of l1 and l2
            newNode = ListNode(smallerVal)
            # since the new node isn't opinting anywhere and nothing is pointing to it, we'll move the pointer to that new node
            ptr.next = newNode
            # now we'll need to move the pointer forward to the newNode
            ptr = ptr.next
        
            
        return head.next

# OPTIMIZED 
    def mergeTwoLists1(self, l1, l2):
        dummy_head = ListNode(0)
        temp = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return dummy_head.next