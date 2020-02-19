class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        num = 0
        
        for i in range(0, len(s) - 1):     # len(s) - 1 because indexes start at 0. need -1 to account for whole str
            if dict[s[i]] < dict[s[i+1]]:  # checks if numeral to the right is larger. 
                num -= dict[s[i]]          # if so, subtract smaller numeral value from the total
            else: 
                num += dict[s[i]]          # else, add numeral value to total
                
        return num + dict[s[-1]]           # takes the total and adds the value of the last numeral

# The way this solution works is it parses the string left to right and considers the Roman numerals in pairs. 
# If the numeral to the right is greater than the numeral to the left, we subtract the current numeral's value from the running total, otherwise we add the numeral's value. 
# At the end we return the running total plus the value of the last numeral; since there can be no numeral to the right of the last numeral we always add it.