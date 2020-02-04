class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0  # keep a running balance of R's and L's. When balance == 0, increase counter by 1

        for i in s:
            if balance == 0:
                count += 1
            if i == "R":
                balance += 1
            if i == "L":
                balance -= 1

        return count