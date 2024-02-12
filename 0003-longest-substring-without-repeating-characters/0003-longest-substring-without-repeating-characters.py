class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        itr = 0
        end_itr = 0
        max_length = 0
        substring_words = []
        while itr < len(s) - max_length:
            if not s[itr+end_itr] in substring_words:
                substring_words.append(s[itr+end_itr])
                max_length = max(max_length, len(substring_words))
                end_itr += 1
            else:
                substring_words = []
                end_itr = 0
                itr+=1

        return max_length