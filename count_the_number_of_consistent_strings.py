class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        output = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                output += 1
        return output