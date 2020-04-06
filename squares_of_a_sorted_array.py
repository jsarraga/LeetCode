# Approach 1:
# square each number, then sort the array


def sortedSquares(A):
    return sorted(x**2 for x in A)


# Approach 2:
# two pointer approach
# bc the arrays are sorted, have one pointer on the left and one pointer on the right. 
# Compare the squares of each element, and take the larger of the squares and append it to the end of the result array
# then move the corresponding pointers 

def sortedSquares1(A):
    write_pointer = len(A) - 1
    left_read_pointer = 0
    right_read_pointer = len(A) - 1
    left_square = A[left_read_pointer] ** 2
    right_square = A[right_read_pointer] ** 2
    
    while write_pointer >= 0:
        if left_square > right_square:
            return_array[write_pointer] = left_square
            left_read_pointer += 1
            left_square = A[left_read_pointer] ** 2
        else:
            return_array[write_pointer] = right_square
            right_read_pointer -= 1
            right_square = A[right_read_pointer] ** 2
        write_pointer -= 1
    return return_array