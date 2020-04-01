
# cheater approach
def isPalindrome(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result == result[::-1]

# Approach:
# find the midpoint
# reverse the second half of the linked list
# check if first half == second half while traversing them

def isPalindrome1(head):
    # find the mid node -> bc fast is going twice as fast as slow, when fast hits the end, slow will hit the middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    # reverse the second half -> slow is head
    node = None
    while slow:
        ptr = slow.next
        slow.next = node
        node = slow
        slow = ptr
        
    
    # compare the first and second half nodes
    while node:
        if head.val != node.val:
            return False
        else:
            head = head.next
            node = node.next
    return True