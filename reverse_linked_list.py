
# Linked List:  1 -> 2 -> 3 -> 4 -> 5 -> None
# need to reverse the pointers, NOT reorder and make a new linked list with 5 as head
# None <- 1 <- 2 <- 3 <- 4 <- 5

def reverseList(head):
        # set prev to None
        prev = None
        while head:
            # need a variable to hold the value of head
            temp = head
            # move head to the next node
            head = head.next
            # change the pointer to prev
            temp.next = prev
            # move prev up to temp 
            prev = temp
        return prev