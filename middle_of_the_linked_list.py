# Approach:
# have one pointer (fast) go through the list twice as fast as the the other (slow)
# by the time the fast pointer hits the end of the list, slow will reach the middle node. return slow

# Two - pointer method
def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# output to an array
def middleNode1(head):
    result = [head]
        
    while result[-1].next:
        result.append(result[-1].next)
    return result[len(result) // 2]