class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        mapping_table = str.maketrans('', '', string.punctuation)
        s = s.translate(mapping_table).replace(' ', '')
        return s == s[::-1]