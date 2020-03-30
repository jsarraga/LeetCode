# Approach:
# make a list of the the linked list values and check if the reverse == original


def isPalindrome(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next

    return result == result[::-1]