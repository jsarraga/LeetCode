class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_digits = 1
        sum_digits = 0

        for i in str(n): # convert to str so e can iterate throught the int
            product_digits = product_digits * int(i)  # find product. convert back to int to multiply
            sum_digits += i                           # find sum. convert back to int to multiply

        return product_digits - sum_digits

    