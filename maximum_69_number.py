class Solution:
    # brute force
    def maximum69Number (self, num: int) -> int:
        max_num = num
        num = str(num)
        
        for i in num:
            if i == "9":
                new_num = num.replace("9","6", 1)
                if int(new_num) > max_num:
                    max_num = int(new_num)
            elif i == "6":
                new_num = num.replace("6","9", 1)
                if int(new_num) > max_num:
                    max_num = int(new_num)
            else:
                return int(num)
            
        return max_num

    # SLIGHTLY optimized solution
    # when iterating through the int, chaning the first 6 to a 9 will suffice. then break to return new num
        # num_list = list(str(num))
        # for i in range(len(num_list)):
        #     if num_list[i] == '6':
        #         num_list[i] = '9'
        #         break
        # return ''.join(num_list)
    